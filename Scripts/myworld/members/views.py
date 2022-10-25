from django.urls import reverse
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Members


def index(request):
    try:
        my_members = Members.objects.all().values()

        template = loader.get_template('index.html')

        # test = {"name":34535, "ok":5345}
        # print(test)
        context = {
            'my_members': my_members,
        }
        return HttpResponse(template.render(context, request))
    except:
        return HttpResponse(template.render())


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
        print(request.POST["first"])
        x = request.POST['first']
        y = request.POST['last']
        member = Members(firstname=x, lastname=y)
        member.save()
        return HttpResponseRedirect(reverse('index'))

    except:
        print(request.POST)
        print(5345)
        return HttpResponse('hello')


def delete_record(request, id):
    try:
        member = Members.objects.get(id=id)
        member.delete()
        return HttpResponseRedirect('/members')
    except:
        return HttpResponse('not found member')


def update(request, id):
    my_member = Members.objects.get(id=id)
    template = loader.get_template('update.html')
    context = {
        'my_member': my_member,
    }
    # try:
    #     member = Members.objects.get(id=id)
    #     print(member.delete())
    #     return HttpResponseRedirect('/members')
    # except:
    return HttpResponse(template.render(context, request))

    # def html_view(request):
    #     template = loader.get_template('myfirst.html')
    #     return HttpResponse(template.render())


def update_record(request, id):

    try:
        first = request.POST['first']
        last = request.POST['last']
        member = Members.objects.get(id=id)
        member.firstname = first
        member.lastname = last
        member.save()
        return HttpResponseRedirect(reverse('index'))
    except:
        return HttpResponse('tl345l34')


def template_test(request):
    # my_members = Members.objects.all().values()
    context = {
        'fruits': ['Apple', 'Banana', 'Cherry', 'Orange']
    }
    template = loader.get_template('template.html')
    return HttpResponse(template.render(context, request))
