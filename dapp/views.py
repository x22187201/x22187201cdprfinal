from django.shortcuts import render,redirect ,get_object_or_404,reverse
from django.db.utils import IntegrityError
from .models import Items,OrderDetail
from .forms import ItemForm, RegistrationForm 
from django.conf import settings
from django.http import JsonResponse,HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
import stripe,json
import boto3
from botocore.exceptions import ClientError
import requests

# Create your views here.

def index(request):
    items = Items.objects.all()
    return render(request,'dapp/index.html',{'items':items})

def detail(request,id):
    item = Items.objects.get(id=id)
    stripe_publishable_key = settings.STRIPE_PUBLISHABLE_KEY

    return render(request, 'dapp/detail.html',{'item':item,'stripe_publishable_key':stripe_publishable_key})

@csrf_exempt
def create_checkout_session(request,id):
    request_data = json.loads(request.body)
    item = Items.objects.get(id=id)
    stripe.api_key = settings.STRIPE_SECRET_KEY 
    customer_email = request_data['email'].strip()

    try:
        checkout_session = stripe.checkout.Session.create(
            customer_email = customer_email,
            payment_method_types = ['card'],
            line_items=[
                {
                    'price_data':{
                        'currency':'usd',
                        'product_data':{
                            'name':item.name
                        },
                        'unit_amount':int(item.price * 100)
                    },
                    'quantity':1
                }
            ],
            mode='payment',
            success_url = request.build_absolute_uri(reverse('success')) +
            "?session_id={CHECKOUT_SESSION_ID}",
            cancel_url =request.build_absolute_uri(reverse('failed')),
        ) 

        order = OrderDetail()
        order.customer_email = customer_email
        order.item = item
        order.stripe_payment_intent = checkout_session.payment_intent
        order.amount = int(item.price)
        order.save()
        return JsonResponse({'sessionId':checkout_session.id})

    except IntegrityError as e:
        return JsonResponse({'error': str(e)}, status=400)
    


def create_item(request):
    if request.method == 'POST':
        item_form = ItemForm(request.POST,request.FILES)
        if item_form.is_valid():
            new_item = item_form.save(commit=False)
            new_item.seller = request.user
            new_item.save()
            return redirect('index')
    item_form = ItemForm()
    return render(request,'dapp/create_item.html',{'item_form':item_form})

def edit_item(request,id):
    item = Items.objects.get(id=id)
    if item.seller != request.user:
        return redirect('invalid')

    item_form = ItemForm(request.POST or None,request.FILES or None,instance = item)
    if request.method=='POST':
        if item_form.is_valid():
            item_form.save()
            return redirect('index')
    return render(request,'dapp/edit_item.html',{'item_form':item_form,'item':item})


def delete_item(request,id):
    item = Items.objects.get(id=id)
    if item.seller != request.user:
        return redirect('invalid')
    if request.method == 'POST':
        item.delete()
        return redirect('index')    
    return render(request,'dapp/delete.html',{'item':item})


def dashboard(request):
    items = Items.objects.filter(seller=request.user)
    return render(request,'dapp/dashboard.html',{'items':items})

def register(request):
    if request.method == 'POST':
        user_form  = RegistrationForm(request.POST)
        new_user = user_form.save(commit=False)
        new_user.set_password(user_form.cleaned_data['password'])
        new_user.save()
        return redirect('login')
    user_form  = RegistrationForm()
    return render(request,'dapp/register.html',{'user_form':user_form})

def invalid(request):
    return render(request,'dapp/invalid.html')



def payment_success_view(request):
    session_id = request.GET.get('session_id')
    print(request)
    print(session_id)
    if session_id is None:
        print(None)
        return HttpResponseNotFound()
    stripe.api_key = settings.STRIPE_SECRET_KEY
    session = stripe.checkout.Session.retrieve(session_id)
    order = get_object_or_404(OrderDetail,stripe_payment_intent= session.payment_intent)
    print(order)
    order.has_paid= True
    order.save()

    return render(request,'dapp/payment_success.html')


def payment_failed_view(request):
    return render(request,'dapp/payment_failed.html')


def add_reviews(rating, comment):

        api_url = "https://rnqv6c1vv8.execute-api.us-east-1.amazonaws.com/STAGE/Reviews"

        params = {
            'rating': rating,
            'comment': comment,
        }

        try:
            response = requests.post(api_url, json=params)

            if response.status_code == 200:
                result = response.json()
                return result
            else:
                error = 'API request failed with status code {}'.format(response.status_code)
                return error
        
        except Exception as e:
            error = 'Failed to connect to the API. Try Again!'
            print('Error',e)
            return error

def convert(request):
    context = {}
    
    if 'review_submit' in request.POST:
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')

        print(request.POST)

        context['review_result'] = add_reviews(rating, comment)
        print([context])
        
    return render(request, 'dapp/add_reviews.html', context)




def convert_time(request):
    context = {}
    
    if 'timezone_submit' in request.POST:
        country = request.POST.get('country')
        city = request.POST.get('city')

        print(request.POST)

        context['timezone_result'] = timezone_converter(country, city)
        print([context])
        
    return render(request, 'dapp/timezone-converter.html', context)
    
def timezone_converter(country, city):

        api_url = "http://www.arunangshunayak.software/api/TimeZone"

        params = {
            'country': country,
            'city': city,
        }

        try:
            response = requests.post(api_url, json=params)

            if response.status_code == 200:
                result = response.json()
                return result
            else:
                error = 'API request failed with status code {}'.format(response.status_code)
                return error
        
        except Exception as e:
            error = 'Failed to connect to the API. Try Again!'

