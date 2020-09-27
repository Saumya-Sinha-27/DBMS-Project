from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from travello.models import Desti
from travello.models import destination

# Create your views here.

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']
        conf_password = request.POST['password2']
        if password == conf_password:
            if User.objects.filter(username=username):
                messages.info(request, 'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email):
                messages.info(request, 'Email exists')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                user.save()
                print("user_created")
                return redirect('login')
        else:
            messages.info(request, 'Password not matching')
            return redirect('register')
        return redirect('/')
    else:
        return render(request, 'register.html');

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/log/'+str(user.id)+'/')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    else:
            return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def add(request, pk, id):
    if id:
        print(pk)
        destina = destination.objects.get(id=pk)
        user = User.objects.get(id=id)
        print(destina.name)
        print(user.username)
        desti = Desti.objects.create(user_id=user, dest_id=destina)
        desti.save();
        return redirect('/log/'+str(user.id)+'/')
    else:
        messages.info(request, 'Please Login First !')
        return redirect('/')



