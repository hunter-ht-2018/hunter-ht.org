# -*- coding:utf-8 -*-
from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect,Http404,render_to_response
from django.contrib import auth
from .models import  *
from django import forms
from .models import User
from .models import Publications
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from django.db.utils import ProgrammingError
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.hashers import make_password
import os


def home(request):
    if not Publications.objects.last():
        return render(request, 'home.html')
    else:
        if Publications.objects.last().pubID>0:
            publications = Publications.objects.filter()
            return render_to_response('home.html',locals())
    return render(request, 'home.html')

def register(request):
    response = JsonResponse({"message":" "})
    if request.is_ajax():
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == '' or password == '':
            response = JsonResponse({"message": "用户名或密码不能为空"})
            return response
        result = User.objects.filter(name=username)
        if result:
            response = JsonResponse({"message": "用户名已存在"})
            return response
        if User.objects.last() is None:
            userID = 1
        else:
            userID = User.objects.last().userID + 1
        try:
            User.objects.create(userID=userID, name=username, pwd=password)
            response = JsonResponse({"message": "添加成功"})
            return response
        except ValidationError as e:
            response = JsonResponse({"message": "###create data wrong####"})
            return response
    return render(request, 'register.html')


def signin(request):
    if request.is_ajax():
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        login_state={}
        try:
            db_info = User.objects.get(name=username)
        except ObjectDoesNotExist as e:
            response = JsonResponse({"message": e})
            return response
        if not db_info:
            response = JsonResponse({"message": "用户不存在"})
            return response
        else:
            if db_info.pwd == password:
                login_state['loginState']='LoginSuccess'
                login_state['username']=db_info.name
                # return render(request, 'index.html', {'username': username, 'password': password})
                response = JsonResponse({"message": "登录成功"})
                return response
                # return render(request,'index.html', {'username': username, 'password': password})
            else:
                response = JsonResponse({"message": "密码错误"})
                return response
    return render(request, 'signin.html')

def index(request):
    if Publications.objects.last():
        if Publications.objects.last().pubID>0:
            publications = Publications.objects.filter()
            return render_to_response('index.html',locals())
    return render(request, 'home.html')

def upload(request):
    if request.method == 'POST':
        myfile = request.FILES.get('myfile', None)
        authors=request.POST.get('authors')
        journalname= request.POST.get('journalname')
        date= request.POST.get('date')
        index= request.POST.get('index')
        if not authors:
            return render(request, 'upload.html',{'uploadMessage':'请按要求填写论文作者'})
        if not myfile:
            return render(request, 'upload.html',{'uploadError':'未选择任何文件'})
        if not myfile.name.endswith('.pdf'):
            return render(request,'upload.html',{'uploadError':'请上传PDF文件'})
        else:
            title=request.POST.get('title')
            if Publications.objects.filter(title=title):
                return render(request, 'upload.html', {'uploadMessage':'已存在该文件，请重命名或删除原文件后再执行该操作'})
        if Publications.objects.last() is None:
            pubID = 1
        else:
            pubID = Publications.objects.last().pubID+1
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        destination = os.path.join(BASE_DIR,'hunter', 'static', 'publications',myfile.name)
        if os.path.exists(destination):
            os.remove(destination)
        with open(destination,'wb+') as dest:
            for chunk in myfile.chunks():
                dest.write(chunk)
            dest.close()
            link=os.path.join('static','publications',myfile.name)
            try:
                Publications.objects.create(pubID=pubID, title=title,link=link, messages='kidding', authors = authors,journalname=journalname,date=date,index=index)
            except ProgrammingError as e:
                return render(request, 'upload.html', {'uploadError':e})
            return render(request, 'upload.html',{'uploadMessage':'上传成功'})
    return render(request, 'upload.html')
