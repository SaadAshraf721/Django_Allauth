from django.contrib.auth import login as abc, authenticate, logout as deff
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from adminapp.models import *


# Create your views here.
def example(request):
    return render(request, 'Sociaal.html')


def index(request):
    return render(request, 'index.html')


@login_required(login_url='/login')
def profile(request):
    return render(request, 'std_profile.html')


@login_required(login_url='/login')
def logout(request):
    deff(request)
    return redirect('/')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        create = User(
            username=username, email=email, first_name=phone, password=make_password(password)
        )
        create.save()
        if create:
            auth = authenticate(username=username, password=password)
            if auth is not None:
                abc(request, auth)
                return redirect('/accounts/profile/')
    form = AuthenticationForm()
    return redirect('/')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        auth = authenticate(username=username, password=password)
        if auth is not None:
            abc(request, auth)
            return redirect('/accounts/profile/')
    form = AuthenticationForm()
    return redirect('/')


def all_examf(request):
    all_exam = Exam.objects.all()
    return render(request, 'all-exam.html', {'exam': all_exam})


def exam_detail(request, id):
    all_exam = Exam.objects.get(id=id)
    return render(request, 'exam-details.html', {'exam': all_exam})
