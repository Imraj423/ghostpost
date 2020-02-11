from ghostpost.models import ghostPost
from django.shortcuts import render
from ghostpost.forms import addPost


def index(request):
    item = ghostPost.objects.all()
    return render(request, 'index.html', {'data': item})


def detail(request):
    item = addPost.objects.all()
    return render(request, 'detail.html', {'data': item})
