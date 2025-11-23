from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
from django.contrib.auth import authenticate,login
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.contrib import messages
# from django.conf
from .models import CustomUserModel
from django.views.decorators.csrf import csrf_exempt
import json

User = get_user_model()
# Create your views here.
@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        email = data.get('email')
        password = data.get('password')

        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'status': 'success', 'message': 'Login successful',"user": {
                    "email": email,
                    "id": user.id,
                }}, status=200)
        else:
            return JsonResponse({'status': 'error', 'message': 'Invalid email or password'}, status=401)
    return JsonResponse({'status': 'error', 'message': 'Only POST requests are allowed'}, status=405)


@csrf_exempt
def register_user(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        name = data.get('name','')
        email = data.get('email')
        password = data.get('password')
        phone = data.get('phone_number')

        first_name, _, last_name = name.partition(' ')

        try:
            user = User.objects.create(
                email=email,
                full_name=name,  
                phone_number=phone, 
                password=make_password(password)
            )
            return JsonResponse({'status': 'success', 'message': 'User registered'}, status=201)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

    return JsonResponse({'status': 'error', 'message': 'Only POST allowed'}, status=405)

def signup_success_page(request):
    return render(request,'user_add_success.html')

