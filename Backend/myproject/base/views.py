# from django.shortcuts import render
# from django.views.generic import View

# class AjaxHandler(View):
#     return render(request, 'login.html')

from .models import CreateLogin
from django.http import HttpResponse
from django.contrib.auth import authenticate

# Create your views here.
def create_user(request):
    firstname=request.GET['firstname']
    lastname=request.GET['lastname']
    username=request.GET['username']
    email=request.GET['email']
    password=request.GET['password']
    
    login_obj = CreateLogin(
        firstname=firstname,
        lastname=lastname, 
        username=username,
        email=email,
        password=password,
        )
        
    login_obj.save()
        
    return HttpResponse("True")
  
def validate_user(request):
    username = request.GET['username']
    
    try:
        CreateLogin.objects.get(username=username)
    except Exception:
        return HttpResponse("No user found")

def check_login(request):
    username=request.GET['username']
    password=request.GET['password']

    user=CreateLogin.objects.get(username=username,password=password)
    if user is not None:
        return HttpResponse("success")
    else:
        return HttpResponse("failed")

    # if ((CreateLogin.objects.username==username or CreateLogin.email==username) and CreateLogin.password==password ):
    #     return HttpResponse("True")
    # else:
    #     return HttpResponse("False")