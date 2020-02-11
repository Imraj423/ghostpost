from ghostpost.models import ghostPost
from django.shortcuts import render
from ghostpost.forms import addPost


def index(request):
    item = ghostPost.objects.all()
    return render(request, 'ghostpost/index.html', {'data': item})


def post(request):
    item = addPost.objects.all()
    return render(request, 'ghostpost/detail.html', {'data': item})
