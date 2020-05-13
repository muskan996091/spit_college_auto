from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import attendance
from django.template import loader

def mainpage(request):
    all_request = attendance.objects.all()
    template = loader.get_template('request/mainpage.html')
    context = {
        'all_request': all_request,
    }
    return HttpResponse(template.render(context, request))

def login(request):
    all_request = attendance.objects.all()
    template = loader.get_template('request/login.html')
    context = {
        'all_request': all_request,
    }
    return HttpResponse(template.render(context, request))

def index(request):
    """html=''
    all_request= attendance.objects.all()
    for request in all_request:
        url='/request/'+request.student_name+'/'
        html += '<a href="'+ url +'">'+ request.student_name +'</a><br>'
        """
    all_request = attendance.objects.all()
    template=loader.get_template('request/index.html')
    context={
        'all_request': all_request,
    }
    return HttpResponse(template.render(context, request))

def detail(request, album_id):
    return HttpResponse("<h2>new page:" +str(album_id))