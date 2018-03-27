from django.shortcuts import render,HttpResponse


# Create your views here.
def marks(request):
    return HttpResponse('academics/templates/base.html')
