from ghostpost.models import ghostPost
from django.shortcuts import render, reverse, HttpResponseRedirect
from ghostpost.forms import addPost


def index(request):
    item = ghostPost.objects.all()
    return render(request, 'index.html', {'data': item})


def detail(request, id):
    item = addPost.objects.get(id=id)
    return render(request, 'detail.html', {'data': item})


def post_add(request):
    html = 'addpost.html'

    if request.method == 'POST':
        form = addPost(request.POST)

        if form.is_valid():
            form.save()
            data = form.cleaned_data
            ghostPost.objects.create(
                title=data['title'],
                message=data['message']
            )
        return HttpResponseRedirect(reverse("index"))
    form = addPost()

    return render(request, html, {'form': form})
