from ghostpost.models import ghostPost
from django.shortcuts import render, reverse, HttpResponseRedirect
from ghostpost.forms import addPost


def index(request):
    item = ghostPost.objects.all()
    return render(request, 'index.html', {'data': item})


def detail(request):
    item = ghostPost.objects.all()
    return render(request, 'detail.html', {'data': item})


def post_add(request):
    html = 'addpost.html'

    if request.method == 'POST':
        form = addPost(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            ghostPost.objects.create(
                message=data['message'],
                

            )
        return HttpResponseRedirect(reverse("index"))
    form = addPost()

    return render(request, html, {'form': form})


def like(request, id):
    post = ghostPost.objects.get(id=id)
    post.like += 1
    post.save()
    return HttpResponseRedirect(reverse('index'))


def dislike(request, id):
    post = ghostPost.objects.get(id=id)
    post.dislike -= 1
    post.save()
    return HttpResponseRedirect(reverse('index'))
