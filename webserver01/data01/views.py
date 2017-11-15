from django.shortcuts import render
from data01.models import PosterData
from data01.models import pd1
from data01.models import pd1_time


# Create your views here.

def test(request):
    return render(request,'data01/test.html',{})

def test_title(request):
    Poster_list=PosterData.objects.exclude(title__exact='')
    return render(request,'data01/test_title.html',{'Poster_list':Poster_list})

def test_pd1(request):
    oneday=pd1.objects.exclude(title__exact='')
    return render(request,'data01/test_pd1.html',{'oneday':oneday})

def test_pd1_time(request):
    time=pd1_time.objects.exclude(title__exact='')
    return render(request,'data01/test_pd1_time.html',{'time':time})
