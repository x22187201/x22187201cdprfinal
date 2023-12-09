from django.shortcuts import render,redirect 
from .models import Items
from .forms import ItemForm, RegistrationForm 

# Create your views here.

def index(request):
    items = Items.objects.all()
    return render(request,'dapp/index.html',{'items':items})

def detail(request,id):
    item = Items.objects.get(id=id)
    return render(request, 'dapp/detail.html',{'item':item})

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

