from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import *


def hello(request):
    _vod=Vodspec.objects.all().order_by('title')
    args= {'vod':_vod}

    return render(request,'vod/templates.html',args)

    # return HttpResponse('salam dostan')
