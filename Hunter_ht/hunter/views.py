# -*- coding:utf-8 -*-
#encoding=utf8
from django.shortcuts import render
import sys
reload(sys)
sys.setdefaultencoding('utf8')
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
import datetime


def home(request):
    if not Publications.objects.last():
        return render(request, 'home.html')
    else:
        if Publications.objects.last().pubID > 0:
            publications = Publications.objects.all()
            articles = Articles.objects.filter(publish="1")
            names = PubToUser.objects.values('username')
            pubAuthors=[]
            for name in names:
                if name['username'] not in pubAuthors:
                    pubAuthors.append(name['username'])
            for publication in publications:
                print publication.pubID
            return render_to_response('home.html',locals())
    return render(request, 'home.html')

def search(request):
    pubs={}
    if request.is_ajax():
        # title = request.POST.get('titlekey')
        # request.body.count()
        author = request.POST.get('authorkey')
        if author=='' or author==None:
            message = JsonResponse({"warning": "搜索内容不能为空"})
            return HttpResponse(json.dumps(message), content_type='application/json')
        else:
            if author == 'All' or author=='':
                pub={}
                message=""
                publications=Publications.objects.all()
                for publication in publications:
                    pub["title"] = str(publication.title)
                    pub["link"] = str(publication.link)
                    pub["authors"] = str(publication.authors)
                    pub["messages"] = str(publication.messages)
                    pub["journalname"] = str(publication.journalname)
                    pub["date"] = str(publication.date)
                    pub["publishType"] = str(publication.publishType.encode('utf-8'))
                    pub["index"] = str(publication.index)
                    message += '{"title":"' + pub["title"] + '","link":"' + pub["link"] + '","authors":"' + pub[
                        "authors"] + '","messages":"' + pub["messages"] + '","publishType":"' + pub[
                                   "publishType"] + '","journalname":"' + pub["journalname"] + '","date":"' + pub[
                                   "date"] + '","index":"' + pub["index"] + '"},'
                message = message.strip(',')
                message = '{"fields":[' + message + ']}'
                return HttpResponse(json.dumps(message), content_type='application/json')
            else:
                try:
                    records = PubToUser.objects.all()
                    list=[]
                    a=author.lower().strip()
                    a_revert = ''
                    if ' ' in a:
                        a_revert= a.split(' ')[1]+a.split(' ')[0]
                    for record in records:
                        r=record.username.lower().strip()
                        r_none_space = r.replace(' ','')
                        r_revert = ''
                        if ' ' in r:
                            r_revert = r.split(' ')[1]+r.split(' ')[0]
                        if record.pubID not in list:
                            if (a in r) or (a_revert !='' and a_revert in r_none_space) or (a in r_none_space) or (a in r_revert):
                                list.append(record.pubID)

                    # pubIDs = PubToUser.objects.filter(username=author)
                    # if pubIDs.count() == 0:
                    #     print "0000"
                    #     message = '{"warning":"0"}'
                    #     return HttpResponse(json.dumps(message), content_type='application/json')
                    message = ""
                    pub = {}
                    # list=[]
                    # for pubID in pubIDs:
                    #     if pubID.pubID not in list:
                    #         list.append(pubID.pubID)
                    for item in list:
                        publication = Publications.objects.get(pubID=item)
                        pub["title"]=str(publication.title)
                        pub["link"] = str(publication.link)
                        pub["authors"] = str(publication.authors)
                        pub["messages"] = str(publication.messages)
                        pub["journalname"] = str(publication.journalname)
                        pub["date"] = str(publication.date)
                        pub["publishType"] = str(publication.publishType.encode('utf-8'))
                        pub["index"] = str(publication.index)
                        message += '{"title":"' + pub["title"] + '","link":"' + pub["link"] + '","authors":"' + pub["authors"] + '","messages":"' + pub["messages"]+ '","publishType":"' + pub["publishType"] + '","journalname":"' + pub["journalname"] + '","date":"' + pub["date"] + '","index":"' + pub["index"] + '"},'
                    message = message.strip(',')
                    message = '{"fields":['+message+']}'
                    return HttpResponse(json.dumps(message), content_type='application/json')
                except ValidationError as e:
                    message = JsonResponse({"warning":e})
                    return message
            # if title !='' and author=='':
            #     try:
            #         publications = Publications.objects.filter(title=title)
            #         for publication in publications:
            #             message = message+"{'title':'"+publication.title+"','authors':'"+publication.authors+"','messages':'"+publication.messages+"','publishType':'"+publication.publishType+"','journalname':'"+publication.journalname+"','date':'"+publication.date+"','index':'"+publication.index+"'},"
            #         message=message+"}"
            #         print message
            #         return HttpResponse(json.dumps(message), content_type='application/json')
            #     except ValidationError as e:
            #             message = JsonResponse({"warning":e})
            #             return message
            #




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
            print articles
            articles = serializers.serialize("json",articles)
            print articles
            return HttpResponse(articles)
    if request.is_ajax():
        title = request.POST.get('title')
        try:
            Articles.objects.filter(title=title).delete()
            response = JsonResponse({"warning":"文章删除成功"});
            return response
        except ProgrammingError as e:
            response = JsonResponse({"warning":"文章删除失败"});
            return response
    if request.POST:
        authors=request.POST.get('authors','')
        myfile = request.FILES.get('myfile', None)
        str='，'.decode('utf-8')
        authors = authors.replace(str,',')
        types=request.POST.get('type')
        journalname= request.POST.get('journalname')
        date= request.POST.get('date')
        index= request.POST.get('index')
        message = {}
        if not authors:
            return render(request, 'index.html',{'uploadMessage':'请按要求填写论文作者'})
        if types=='0':
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
                print types
                Publications.objects.create(pubID=pubID, title=title,link=link, messages='kidding', authors = authors, publishType=types.encode('utf-8'), journalname=journalname,date=date,index=index)
            except ProgrammingError as e:
                return render(request, 'index.html', {'uploadError':'Publications表错误：' + e})
            authorArr = authors.split(',')
            for author in authorArr:
                try:
                    PubToUser.objects.create(pubID = pubID,username=author)
                except ProgrammingError as e:
                    return render(request, 'index.html', {'uploadError': 'PubToUser数据表错误：' + e})
            uploadMessage = '文件上传成功'
            publications = Publications.objects.filter()
            return render_to_response('index.html', locals())
    if Publications.objects.last():
        if Publications.objects.last().pubID>0:
            publications = Publications.objects.all()
            return render_to_response('index.html',locals())
    return render(request, 'index.html')


def view(request):
    if request.method=="GET":
        if 'title' in request.GET:
            title = request.GET.get('title')
            article = Articles.objects.get(title=title).content
            authorID=Articles.objects.get(title=title).authorID
            authorname = User.objects.get(userID=authorID).name
            # jsonStr = '[{"view"：{"title":'+title+',"article":'+article+',"authorname":'+authorname+'}}]'
            return render_to_response("view.html",locals())


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
    if request.method == "GET":
        if 'title' in request.GET:
            title = request.GET.get('title')
            articleCnt = Articles.objects.get(title = title).content
            return render_to_response("write.html",locals())
    if request.is_ajax():
        username = request.POST.get('username','')
        title = request.POST.get('title','')
        content = request.POST.get('content','')
        publish = request.POST.get('publish','')
        editdatetime = datetime.datetime.now().date()
        print editdatetime
        #加入判断题目是否相同
        isHave = Articles.objects.filter(title=title)
        isNew = request.POST.get('isNew')
        oldtitle=request.POST.get('oldtitle')
        print isHave
        print isNew
        if isHave and isNew=='1':
            response = JsonResponse({"warning":"该文章题目已存在"})
            return response
        else:
            if isNew == '0':
                try:
                    Articles.objects.filter(title=oldtitle).update(title=title,content=content,publish=publish,editDateTime = editdatetime)
                    if publish == '0':
                        response = JsonResponse({"warning": "文章更新已保存，尚未发布"})
                        return response
                    else:
                        response = JsonResponse({"warning": "文章更新已发布成功"})
                        return response
                except ProgrammingError as e:
                    response = JsonResponse({"warning":e})
                    return response
        if Articles.objects.last() is None:
            articleID = 1
        else:
            articleID = Articles.objects.last().articleID+1
        try:
            authorID = User.objects.get(name=username).userID
            if not authorID:
                response = JsonResponse({"warning": "该作者不存在"})
                return response
            else:
                try:
                    Articles.objects.create(articleID=articleID, authorID=authorID, title=title, content=content,publish=publish,editDateTime=editdatetime)
                    if publish == '0':
                        response = JsonResponse({"warning": "文章保存成功"})
                    else:
                        response = JsonResponse({"warning": "文章发布成功"})
                except EOFError as e:
                    response = JsonResponse({"warning": e})
                return response
        except ObjectDoesNotExist as e:
            response = JsonResponse({"warning": e})
            return response

    return render(request,'write.html')
