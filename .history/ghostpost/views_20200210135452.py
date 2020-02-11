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
                message=data['message']
            )
        return HttpResponseRedirect(reverse("index"))
    form = addPost()

    return render(request, html, {'form': form})


def like(request, post_id):
    if request.method == 'POST':
        post = ghostPost.objects.get(pk=post_id)
        post.likes += 1
        post.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def unlike(request, post_id):
    if request.method == 'POST':
        post = ghostPost.objects.get(pk=post_id)
        post.likes -= 1
        post.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
