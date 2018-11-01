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
    url(r'^write/$',views.write),
    url(r'^home/view/',views.view),
    url(r'^search/',views.search),
    url(r'^profile/[a-zA-Z0-9]+.html', views.personal),
    url(r'^edit/[a-zA-Z0-9]+.html', views.editPro),
    url(r'^view/',views.view),
    url(r'^/static/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),
    url(r'^home/static/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),
]
