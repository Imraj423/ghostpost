from ghostpost.models import ghostPost
from django.shortcuts import render
from ghostpost.forms import addPost


def index(request):
    item = ghostPost.objects.all()
    return render(request, 'index.html', {'data': item})


def detail(request):
    item = ghostPost.objects.all()
    return render(request, 'detail.html', {'data': item})


def addPost(request):
    html = 'addpost.html'

    if request.method == 'POST':
        form = addPost(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            ghostPost.objects.create(
                title=data['title'],
                message=data['message']
            )

    form = addPost()

    return render(request, html, {'form': form})
