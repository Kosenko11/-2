from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import DesignRequestForm, RegisterForm


def index(request):
    return render(request, "user/index.html")

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("index")
        else:
            messages.error(request, "Ошибка регистрации. Проверьте данные.")
    else:
        form = RegisterForm()
    return render(request, "user/register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            messages.error(request, "Неверный логин или пароль")
    return render(request, "user/user_login.html")

def logout_view(request):
    logout(request)
    return redirect("index")


from django.contrib.auth.decorators import login_required
from .models import DesignRequest
from django.urls import reverse


@login_required
def dashboard(request):
    return render(request, 'user/dashboard.html')

@login_required
def create_request(request):
    if request.method == 'POST':
        form = DesignRequestForm(request.POST)
        if form.is_valid():
            dr = form.save(commit=False)
            dr.user = request.user
            dr.save()
            return redirect('request_list')
    else:
        form = DesignRequestForm()
    return render(request, 'user/create_request.html', {'form': form})

@login_required
def request_list(request):
    requests = DesignRequest.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'user/request_list.html', {'requests': requests})

@login_required
def delete_request(request, pk):
    dr = get_object_or_404(DesignRequest, pk=pk, user=request.user)
    if request.method == 'POST':
        dr.delete()
        return redirect('request_list')
    return render(request, 'user/confirm_delete.html', {'request_obj': dr})

