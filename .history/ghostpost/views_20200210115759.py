from ghostpost.models import ghostPost
from django.shortcuts import render, reverse, HttpResponseRedirect


def index(request):
    item = ghostPost.objects.all()
    return render(request, 'index.html', {'data': item})

