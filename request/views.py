from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import attendance
from django.template import loader
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

#-----------------------------------------

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

#-----------------------------------------

def slogin(request):
    all_request = attendance.objects.all()
    template = loader.get_template('request/slogin.html')
    context = {
        'all_request': all_request,
    }
    return HttpResponse(template.render(context, request))

def soption(request):
    all_request = attendance.objects.all()
    template = loader.get_template('request/soptions.html')
    context = {
        'all_request': all_request,
    }
    return HttpResponse(template.render(context, request))

def stud_request(request):
    all_request = attendance.objects.all()
    template = loader.get_template('request/stud_request.html')
    context = {
        'all_request': all_request,
    }
    return HttpResponse(template.render(context, request))

#-----------------------------------------

def key_login(request):
    all_request = attendance.objects.all()
    template = loader.get_template('request/key_login.html')
    context = {
        'all_request': all_request,
    }
    return HttpResponse(template.render(context, request))

def key_request(request):
    all_request = attendance.objects.all()
    template = loader.get_template('request/key_request.html')
    context = {
        'all_request': all_request,
    }
    return HttpResponse(template.render(context, request))

def key_teacher(request):
    all_request = attendance.objects.all()
    template = loader.get_template('request/key_teacher.html')
    context = {
        'all_request': all_request,
    }
    return HttpResponse(template.render(context, request))

#-----------------------------------------

def alum_announce(request):
    all_request = attendance.objects.all()
    template = loader.get_template('request/alum_announce.html')
    context = {
        'all_request': all_request,
    }
    return HttpResponse(template.render(context, request))

def alum_login(request):
    all_request = attendance.objects.all()
    template = loader.get_template('request/alum_login.html')
    context = {
        'all_request': all_request,
    }
    return HttpResponse(template.render(context, request))

def alum_options(request):
    all_request = attendance.objects.all()
    template = loader.get_template('request/alum_options.html')
    context = {
        'all_request': all_request,
    }
    return HttpResponse(template.render(context, request))

def alum_results(request):
    all_request = attendance.objects.all()
    template = loader.get_template('request/alum_results.html')
    context = {
        'all_request': all_request,
    }
    return HttpResponse(template.render(context, request))

def alum_search(request):
    all_request = attendance.objects.all()
    template = loader.get_template('request/alum_search.html')
    context = {
        'all_request': all_request,
    }
    return HttpResponse(template.render(context, request))

#-----------------------------------------

def detail(request, album_id):
    return HttpResponse("<h2>new page:" +str(album_id))

class CreateRequest(CreateView):
    model = attendance
    fields = ['student_name','student_class','requbranch','reason','start_date','end_date']
    labels=['Name','Class','Branch','Reason','Start Date','End Date']
    initial = {'isapproved': False}

class UpdateRequest(UpdateView):
    model = attendance
    fields = ['student_name','reason']

class DeleteRequest(DeleteView):
    model = attendance
    success_url = reverse_lazy('request')
