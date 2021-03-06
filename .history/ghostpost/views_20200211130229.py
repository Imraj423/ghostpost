
from django.shortcuts import render
from django.contrib.auth.models import User
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
                is_Boast=data['is_Boast']
            )
        return HttpResponseRedirect(reverse("index"))
    form = addPost()

    return render(request, html, {'form': form})


def like(request, id):
    post = ghostPost.objects.get(id=id)
    post.like += 1
    post.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def dislike(request, id):
    post = ghostPost.objects.get(id=id)
    post.like -= 1
    post.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def sorted(request):
    html = "index.html"
    data = ghostPost.objects.all().order_by(
        "-like")
    return render(request, html, {"data": data})


def sortedt(request):
    html = "index.html"
    data = ghostPost.objects.all().order_by("-time")
    return render(request, html, {"data": data})


def sortedb(request):
    html = "index.html"
    data = ghostPost.objects.all().order_by("-is_Boast")
    return render(request, html, {"data": data})


def sortedr(request):
    html = "index.html"
    data = ghostPost.objects.all().order_by("-is_Boast").reverse()
    return render(request, html, {"data": data})


def boast(request):
    html = 'index.html'
    data = ghostPost.objects.filter(is_Boast=True).order_by('-time')
    return render(request, html, {'data': data})


def roast(request):
    html = 'index.html'
    data = ghostPost.objects.filter(is_Boast=False).order_by('-time')
    return render(request, html, {'data': data})
