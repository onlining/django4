from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib import auth
from .models import User

# Create your views here.


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    
    elif request.method == 'POST':
        user_id=request.POST.get('id','')
        user_pw=request.POST.get('pw','')
        user_pw_confirm=request.POST.get('pw-confirm','')
        user_name=request.POST.get('name','')
        user_email=request.POST.get('email','')

        if (user_id or user_pw or user_pw_confirm or user_name or user_email)=='':
            return redirect('/accounts/signup')
        elif user_pw != user_pw_confirm:
            return redirect('/accounts/signup')
        else:
            user = User(
                user_id=user_id,
                user_pw=user_pw,
                user_name=user_name,
                user_email=user_email
            )
            user.save()
        return redirect('/login')





def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('django6:django5')
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'login.html')

