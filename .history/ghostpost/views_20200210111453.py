from ghostpost.models import ghostPost
from django.shortcuts import render


def index(request):
    item = ghostPost.objects.all()
    return render(request, 'ghostpost/index.html', {'data': item})

def post(request):
    pass