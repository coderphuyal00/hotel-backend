from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_user, name='user-login'),
    path('signup/', views.register_user, name='user-register'),
    path('signup/success/', views.signup_success_page, name='user-add-success')

]