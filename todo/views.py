from django.shortcuts import render, redirect 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login

# Create your views here.
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

def currenttodos(request):
    return render (request,'currenttodos.html')