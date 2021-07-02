from django.shortcuts import redirect, render 
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index(request):
    if request.user.is_anonymous:
        return redirect('/login')
    return render(request, 'index.html')

def userLogin(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        
        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect('/')
        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')
    return render(request, 'login.html')

def userLogout(request):
    logout(request)
    return redirect('/login')