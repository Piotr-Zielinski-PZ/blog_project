from django.urls import path, include
from . import views

app_name = 'Login_API'

urlpatterns = [
    path('sign_up/', views.sign_up, name='sign_up'),
    path('login_page/', views.login_page, name='login_page'),
    path('logout_page/', views.logout_page, name='logout_page'),
    path('profile/', views.profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('edit_password/', views.edit_password, name='edit_password'),
    path('add_profile_pic/', views.add_profile_pic, name='add_profile_pic'),
    path('edit_profile_pic/', views.edit_profile_pic, name='edit_profile_pic'),

]
