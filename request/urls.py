from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.mainpage, name='index'),
    url(r'^login_attend/$', views.login, name='index'),
    url(r'^request$', views.index, name='index'),
    url(r'^request/(?P<album_id>([A-Z]|[a-z])+)/$', views.detail, name='detail'),
    ]