from django.shortcuts import render, redirect 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def index(request):
    return render(request,'home.html')


def signupuser(request):

    if request.method == 'POST':
        # create a new user
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'],password = request.POST['password1'])
                user.save()
                login(request,user)
                return redirect('currenttodos')

            except IntegrityError:
                return render(request,'signup.html',{'form':UserCreationForm(),'error':"Username already exist"})

        else:
            return render(request,'signup.html',{'form':UserCreationForm(),'error':"passwords didn't match"})

    else:
        return render(request,'signup.html',{'form':UserCreationForm()})

def loginuser(request):
    if request.method == 'POST':
       
        user = authenticate(request, username = request.POST['username'], password = request.POST['password'])
        if user is None:
            return render (request,'login.html',{'form':AuthenticationForm(),'error':'username or password is incorrect'})
        else:
            login(request,user)
            return redirect('currenttodos')
    else:
        return render (request,'login.html',{'form':AuthenticationForm()})

def logoutuser(request):

    if request.method == 'POST':
        logout(request)
        return redirect('/')
        

    

def currenttodos(request):
    return render (request,'currenttodos.html')