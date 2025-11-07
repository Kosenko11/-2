from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import RegistrationForm, LoginForm, RequestForm
from .models import Request

def index(request):
    return render(request, 'user/index.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.first_name = form.cleaned_data['full_name']
            user.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'user/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')
    else:
        form = LoginForm()
    return render(request, 'user/user_login.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('index')

@login_required
def profile(request):
    user_requests = request.user.requests.all()
    return render(request, 'user/dashboard.html', {'requests': user_requests})

@login_required
def create_request(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            req = form.save(commit=False)
            req.user = request.user
            req.save()
            return redirect('profile')
    else:
        form = RequestForm()
    return render(request, 'user/create_request.html', {'form': form})

@login_required
def delete_request(request, pk):
    req = get_object_or_404(Request, pk=pk, user=request.user)
    if request.method == 'POST':
        req.delete()
        return redirect('profile')
    return render(request, 'user/delete_request.html', {'request_obj': req})


def staff_check(user):
    return user.is_authenticated and (user.is_staff or user.is_superuser)
