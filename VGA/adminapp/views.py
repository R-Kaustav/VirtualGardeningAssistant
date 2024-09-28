from django.contrib import messages
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from django.shortcuts import render
def WelcomePage(request):
    return render(request, 'adminapp/WelcomePage.html')

def projecthomepage(request):
    return render(request, 'adminapp/ProjectHomePage.html')


def userprojecthomepage(request):
    return render(request, 'userapp/UserProjectHomePage.html')



def Login(request):
    return render(request,'adminapp/Login.html')
def Register(request):
   return render(request,'adminapp/Register.html')

from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.shortcuts import render
def UserRegisterPageCall(request):
    return render(request, 'adminapp/Register.html')
def UserRegisterLogic(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'OOPS! Username already taken.')
                return render(request, 'adminapp/Register.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'OOPS! Email already registered.')
                return render(request, 'adminapp/Register.html')
            else:
                user = User.objects.create_user(
                    username=username,
                    password=pass1,
                    first_name=first_name,
                    last_name=last_name,
                    email=email
                )
                user.save()
                messages.info(request, 'Account created Successfully!')
                return redirect('UserLoginPageCall')
        else:
            messages.info(request, 'Passwords do not match.')
            return render(request, 'adminapp/Register.html')
    else:
        return render(request, 'adminapp/Register.html')



def UserLoginPageCall(request):
    return render(request, 'adminapp/Login.html')


def UserLoginLogic(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Check the length of the username
            if len(username) == 5:
                # Redirect to StudentHomePage
                messages.success(request, 'Login successful as User!')
                return redirect('UserProjectHomePage')  # Replace with your student homepage URL name
            elif len(username) == 1:

                messages.success(request, 'Login successful as admin!')
                return redirect('projecthomepage')
            else:
                # Invalid username length
                messages.error(request, 'Username length does not match student or faculty criteria.')
                return render(request, 'adminapp/Login.html')
        else:
            # If authentication fails
            messages.error(request, 'Invalid username or password.')
            return render(request, 'adminapp/Login.html')
    else:
        return render(request, 'adminapp/Login.html')