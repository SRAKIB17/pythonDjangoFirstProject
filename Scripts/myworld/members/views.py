from re import template
from django.shortcuts import render
from django.urls import reverse

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Members


def index(request):
    my_members = Members.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'my_members': my_members,
    }
    return HttpResponse(template.render(context, request))


# def members(request):
#     my_members = Members.objects.all().values()
#     template = loader.get_template('index.html')
#     context = {
#         'my_members': my_members,
#     }

#     return HttpResponse(template.render(context, request))


def add(request):
    print(request)
    template = loader.get_template('add.html')
    return HttpResponse(template.render({}, request))


def add_record(request):
    try:
        print(request.POST)
        x = request.POST['first']
        y = request.POST['last']
        # member = Members(firstname=x, lastname=y)
        # member.save()
        return HttpResponseRedirect(reverse('index'))

    except:
        print(request.POST)
        print(5345)
        return HttpResponse('hello')


# def html_view(request):
#     template = loader.get_template('myfirst.html')
#     return HttpResponse(template.render())
