from django.conf.urls import url
from . import views
from Hunter_ht import settings
from django.views.static import serve

urlpatterns = [
    url(r'^$', views.home),
    url(r'^home/$', views.home),
    url(r'^signin/$',views.signin),
    url(r'^index/$',views.index),
    url(r'^admin/$',views.admin),
    url(r'^operator/$', views.operator),
    url(r'^upload/$',views.upload),
    url(r'^uploadImg/$',views.uploadImg),
    url(r'^write/$',views.write),
    url(r'^home/view/',views.view),
    url(r'^search/',views.search),
    url(r'^add_sub_score/',views.add_sub_score),
    url(r'^profile/[a-zA-Z0-9]+.html', views.personal),
    url(r'^home/profile/[a-zA-Z0-9]+.html', views.personal),
    url(r'^edit/[a-zA-Z0-9]+.html', views.editPro),
    url(r'^view/',views.view),
    url(r'^articles/',views.articles),
    url(r'^operatePub/',views.operatePub),
    url(r'^/static/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),
    url(r'^home/static/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),
]
