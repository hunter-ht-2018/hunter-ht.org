# -*- coding:utf-8 -*-
from django.shortcuts import render

# Create your views here.

#from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import auth
from .models import  *
from django import forms
from .models import User
from django.http import HttpResponseRedirect
from django.core.exceptions import ValidationError


def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == '' or password == '':
            return render (request,'register.html', {'message':'用户名或密码不能为空'})
        result = User.objects.filter(name = username)
        if result:
            return render(request,'register.html', {'message':'用户名已存在'})
        if User.objects.last() is None:
            userID=1
        else:
            userID=User.objects.last().userID + 1
        try:
            User.objects.create(userID=userID, name=username, pwd=password,)
        except ValidationError as e:
            error = "###create data wrong####"
            return render(request, 'register.html', {'message': error})
    return render(request,'register.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        login_state={}
        print username,password
        try:
            db_info = User.objects.get(name=username)
        except ValidationError as e:
            return render(request, 'signin.html', {'login_error': e})
        if not db_info:
            return render(request, 'signin.html', {'login_error': '用户不存在'})
        else:
            if db_info.pwd == password:
                login_state['loginState']='LoginSuccess'
                login_state['username']=db_info.name
                return render(request, 'index.html', {'username': username, 'password': password})
            else:
                return render(request, 'signin.html', {'login_error': '密码错误'})

        # if re is not None:
        #     auth.login(request,re)
        #     return render(request,'testPro.html',{'username':username, 'password':password})
        # else:
        #     return render(request,'signin.html',{'login_error':'用户名或密码错误'})
    return render(request, 'signin.html')

def index(request):
    return render(request,'index.html',{'username':'this is Name', 'password':'this is pwd'})