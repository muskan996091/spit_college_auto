from django.conf.urls import url
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns=[
    url(r'^$', views.mainpage, name='index'),
    url(r'^login_attend/$', views.login, name='index'),
    url(r'^login_stud/$', views.slogin, name='index'),
    url(r'^request$', views.index, name='index'),
    url(r'^soptions$', views.soption, name='index'),
    url(r'^stud_request$', views.stud_request, name='index'),
    url(r'^key_login/$', views.key_login, name='index'),
    url(r'^key_request/$', views.key_request, name='index'),
    url(r'^key_teacher$', views.key_teacher, name='index'),
    url(r'^alum_announce$', views.alum_announce, name='index'),
    url(r'^alum_login$', views.alum_login, name='index'),
    url(r'^alum_search$', views.alum_search, name='index'),
    url(r'^alum_options$', views.alum_options, name='index'),
    url(r'^alum_results$', views.alum_results, name='index'),
    url(r'^request/add/$', views.CreateRequest.as_view(), name='add request'),
    url(r'^request/(?P<album_id>([A-Z]|[a-z])+)/$', views.detail, name='detail'),
    ]

urlpatterns += staticfiles_urlpatterns()