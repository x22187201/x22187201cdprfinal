from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index,name='index'),
    path('item/<int:id>',views.detail,name='detail'),
    path('createitem/',views.create_item,name='createitem'),
    path('edititem/<int:id>',views.edit_item,name='edititem'),
    path('delete/<int:id>',views.delete_item,name='delete'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('register/',views.register,name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='dapp/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='dapp/logout.html'),name='logout'),
    path('invalid/',views.invalid, name='invalid'),



]