# -*- coding:utf-8 -*-
#encoding=utf8
from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect,Http404,render_to_response
from django.contrib import auth
from .models import  *
from django import forms
from django.core import serializers
from .models import User
from .models import Publications
from .models import PubToUser
from .models import Articles
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from django.db.utils import ProgrammingError
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect
import string
from django.contrib.auth.hashers import make_password
import os
import json


def home(request):
    if not Publications.objects.last():
        return render(request, 'home.html')
    else:
        if Publications.objects.last().pubID > 0:
            publications = Publications.objects.all()
            articles = Articles.objects.filter(publish="1")
            for publication in publications:
                print publication.pubID
            return render_to_response('home.html',locals())
    return render(request, 'home.html')


def admin(request):
    if User.objects.last():
        if User.objects.last().userID > 0:
            users = User.objects.all()
            for user in users:
                if user.identity=='0':
                    user.identity = '普通用户'
                else:
                    user.identity = '管理员'
            return render_to_response('admin.html',locals())
def operator(request):
    message={}
    if request.is_ajax():
        actiontype = request.POST.get('actiontype')
        if actiontype == '0':
            username = request.POST.get('username')
            password = request.POST.get('password')
            if username == '' or password == '':
                message["warning"] = "用户名或密码不能为空"
                return HttpResponse(json.dumps(message), content_type='application/json')
            result = User.objects.filter(name=username)
            if result:
                message["warning"] = "用户名已存在"
                return HttpResponse(json.dumps(message), content_type='application/json')
            if User.objects.last() is None:
                userID = 1
            else:
                userID = User.objects.last().userID + 1
            try:
                userAdd=User.objects.create(userID=userID, name=username, pwd=password)
                message["warning"]="添加成功"
                users = User.objects.all()
                userList = []
                for user in users:
                    userList.append(user.name)
                message["users"] = userList
                return HttpResponse(json.dumps(message), content_type='application/json')
            except ValidationError as e:
                message["warning"]=e;
                return HttpResponse(json.dumps(message), content_type='application/json')
        if actiontype == '1':
            delname = request.POST.get('delname')
            try:
                delrestlt = User.objects.filter(name=delname).delete()
                message["warning"] = "删除成功"
                users = User.objects.all()
                userList = []
                for user in users:
                    userList.append(user.name)
                message["users"] = userList
                return HttpResponse(json.dumps(message), content_type='application/json')
                # return render_to_response('admin.html',locals())
            except:
                message["warning"]="删除出错"
                return HttpResponse(json.dumps(message), content_type='application/json')
        if actiontype == '2':
            resetPwd = request.POST.get('resetPwd')
            resetname = request.POST.get('resetname')
            try:
                User.objects.filter(name=resetname).update(pwd=resetPwd)
                message["warning"]="密码更新成功"
                return HttpResponse(json.dumps(message), content_type='application/json')
            except:
                message["warning"]="密码更新错误"
                return HttpResponse(json.dumps(message), content_type='application/json')
        if actiontype == '3':
            identity = request.POST.get('identity')
            username = request.POST.get('username')
            try:
                User.objects.filter(name=username).update(identity=identity)
                print (identity)
                message["flag"]="1";
                message["warning"]="权限更改成功"
                return HttpResponse(json.dumps(message), content_type='application/json')
            except:
                message["warning"]="权限更改错误"
                message["flag"]="1";
                return HttpResponse(json.dumps(message), content_type='application/json')

    return render_to_response('admin.html', locals())

def add_user(request):
    if request.is_ajax():
        username = request.POST.get('username')
        password = request.POST.get('password')
        message={}
        if username == '' or password == '':
            # message["warning"]="用户名或密码不能为空"
            # response = JsonResponse({"message": "用户名或密码不能为空"})
            return render(request, 'admin.html', {'message': '用户名或密码不能为空'})
        result = User.objects.filter(name=username)
        if result:
            # message["warning"] = "用户名已存在"
            # response = JsonResponse({"message": "用户名已存在"})
            return render(request, 'admin.html',{'message':'用户名已存在'})
        if User.objects.last() is None:
            userID = 1
        else:
            userID = User.objects.last().userID + 1
        userAdd=User.objects.create(userID=userID, name=username, pwd=password)
        if userAdd:
            # message["warning"]="添加成功"
            return render(request, 'admin.html',{'message':'添加成功'})
        else:
            # message["warning"]="添加失败"
            return render(request, 'admin.html',{'message':'添加失败'})
        # try:
        #     User.objects.create(userID=userID, name=username, pwd=password)
            # response = JsonResponse({"message": "添加成功"})
            # return HttpResponse(json.dumps(message), content_type='application/json')
        # except ValidationError as e:
        #     message["warning"] = e
            # response = JsonResponse({"message": e})
    return render(request, 'admin.html')


# def delete_user(request):
#     if request.is_ajax():
#         username = request.POST.get('username')



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
                identity = db_info.identity;
                response = JsonResponse({"message": "登录成功","identity":identity})
                return response
                # return render(request, 'index.html', {'username': username})
            else:
                response = JsonResponse({"message": "密码错误"})
                return response
    return render(request, 'signin.html')

def index(request):
    if request.method=="GET":
        if 'user' in request.GET:
            username = request.GET.get('user')
            userID = User.objects.get(name=username).userID
            articles = Articles.objects.filter(authorID = userID)
            articles = serializers.serialize("json",articles)
            print articles
            return HttpResponse(articles)
    if Publications.objects.last():
        if Publications.objects.last().pubID>0:
            publications = Publications.objects.all()
            return render_to_response('index.html',locals())
    if request.POST:
        authors=request.POST.get('authors','')
        myfile = request.FILES.get('myfile', None)
        str='，'.decode('utf-8')
        authors = authors.replace(str,',')
        type=request.POST.get('type')
        journalname= request.POST.get('journalname')
        date= request.POST.get('date')
        index= request.POST.get('index')
        message = {}
        if not authors:
            return render(request, 'index.html',{'uploadMessage':'请按要求填写论文作者'})
        if type=='0':
            return render(request, 'index.html',{'uploadMessage':'请选择出版类型'})
        if not myfile:
            return render(request, 'index.html',{'uploadError':'未选择任何文件'})
        if not myfile.name.endswith('.pdf'):
            return render(request,'index.html',{'uploadError':'请上传PDF文件'})
        else:
            title=request.POST.get('title')
            if Publications.objects.filter(title=title):
                return render(request, 'index.html', {'uploadMessage':'已存在该文件，请重命名或删除原文件后再执行该操作'})
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
                Publications.objects.create(pubID=pubID, title=title,link=link, messages='kidding', authors = authors, publishType=type, journalname=journalname,date=date,index=index)
            except ProgrammingError as e:
                return render(request, 'index.html', {'uploadError':'Publications表错误：' + e})
            authorArr = authors.split(',')
            for author in authorArr:
                try:
                    PubToUser.objects.create(pubID = pubID,username=author)
                    uploadMessage = '文件上传成功'
                    publications = Publications.objects.filter()
                    return render_to_response('index.html', locals())
                except ProgrammingError as e:
                    return render(request, 'index.html', {'uploadError': 'PubToUser数据表错误：' + e})
    return render(request, 'index.html')

#目前这段代码没有用到
def upload(request):
    if request.POST:
        authors=request.POST.get('authors','')
        myfile = request.FILES.get('myfile', None)
        str='，'.decode('utf-8')
        authors = authors.replace(str,',')
        journalname= request.POST.get('journalname')
        date= request.POST.get('date')
        index= request.POST.get('index')
        message = {}
        if not authors:
            # message["warning"] = "请按要求填写论文作者"
            # return HttpResponse(json.dumps(message), content_type='application/json')
            return render(request, 'index.html',{'uploadMessage':'请按要求填写论文作者'})
        if not myfile:
            # message["warning"] = "未选择任何文件"
            # return HttpResponse(json.dumps(message), content_type='application/json')
            return render(request, 'index.html',{'uploadError':'未选择任何文件'})
        if not myfile.name.endswith('.pdf'):
            # message["warning"] = "请上传PDF文件"
            # return HttpResponse(json.dumps(message), content_type='application/json')
            return render(request,'index.html',{'uploadError':'请上传PDF文件'})
        else:
            title=request.POST.get('title')
            if Publications.objects.filter(title=title):
                # message["warning"] = "已存在该文件，请重命名或删除原文件后再执行该操作"
                # return HttpResponse(json.dumps(message), content_type='application/json')
                return render(request, 'index.html', {'uploadMessage':'已存在该文件，请重命名或删除原文件后再执行该操作'})
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
                # message["warning"] = "Publications表错误:"+e
                # return HttpResponse(json.dumps(message), content_type='application/json')
                return render(request, 'index.html', {'uploadError':'Publications表错误：' + e})
            authorArr = authors.split(',')
            for author in authorArr:
                try:
                    PubToUser.objects.create(pubID = pubID,username=author)
                    return redirect(request, 'index.html', {'uploadMessage': '文件上传成功'})
                except ProgrammingError as e:
                    # message["warning"] = "PubToUser数据表错误:"+e
                    # return HttpResponse(json.dumps(message), content_type='application/json')
                    return render(request, 'index.html', {'uploadError': 'PubToUser数据表错误：' + e})
            # message["warning"] = "上传成功"
            # return HttpResponse(json.dumps(message), content_type='application/json')
    return redirect(request, 'index.html')

# markdown编辑
def write(request):
    if request.is_ajax():
        username = request.POST.get('username','')
        title = request.POST.get('title','')
        content = request.POST.get('content','')
        publish = request.POST.get('publish','')
        if Articles.objects.last() is None:
            articleID = 1
        else:
            articleID = Articles.objects.last().articleID+1
        try:
            authorID = User.objects.get(name=username).userID
        except ObjectDoesNotExist as e:
            response = JsonResponse({"warning": e})
            return response
        if not authorID:
            response = JsonResponse({"warning": "该作者不存在"})
            return response
        else:
            try:
                Articles.objects.create(articleID=articleID, authorID = authorID, title = title, content = content,publish=publish)
                if publish == '0':
                    response = JsonResponse({"warning": "文章保存成功"})
                else:
                    response = JsonResponse({"warning": "文章发布成功"})
            except EOFError as e:
                response = JsonResponse({"warning":e})
            return response
    return render(request,'write.html')
