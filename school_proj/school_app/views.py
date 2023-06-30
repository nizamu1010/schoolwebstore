from django.contrib import messages ,auth
from django.shortcuts import render, redirect
from django.contrib.auth.models import User


def home(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username,password=password)
        
        if user is not None:
            auth.login(request,user)
            # return redirect('/')
            return render(request, 'getform.html')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
        
    return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        u_name = request.POST['username']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']

        if pass1 == pass2:

            if User.objects.filter(username=u_name).exists():
                messages.info(request, "Username taken.")
                return redirect('signup')
            else:
                user = User.objects.create_user(username=u_name, password=pass1)
                user.save()
                return redirect('login')

            # print('user created')

        else:
            messages.info(request, 'password is not matched')
            return redirect('signup')

        return redirect('/')
    return render(request, 'register.html')


def form_view(request):
    if request.method == 'POST':

        name = request.POST.get('name')
        dob = request.POST.get('dob')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        department = request.POST.get('department')
        courses = request.POST.get('courses')
        purpose = request.POST.get('purpose')
        materials = request.POST.getlist('materials')

        message = "Order Confirmed"
        return render(request, 'confirmation.html', {'message': message})   
     
    return render(request, 'form.html')

from django.shortcuts import render, redirect

def signout(request):
    auth.logout(request)
    return redirect('/')

    