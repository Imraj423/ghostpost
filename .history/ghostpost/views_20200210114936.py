from ghostpost.models import ghostPost
from django.shortcuts import render, reverse, HttpResponseRedirect
from ghostpost.forms import addPost


def index(request):
    item = ghostPost.objects.all()
    return render(request, 'index.html', {'data': item})


def detail(request):
    item = addPost.objects.all()
    return render(request, 'detail.html', {'data': item})


def post_add(request):
    html = 'addPost.html'

    if request.method == 'POST':
        form = addPost(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            forms.objects.create(
                title=data['title'],
                isRoast=data['isRoast'],
                submitDate=data['submitDate'],
                message=data['message'],
                upvote=data['upvote'],
                downvote=data['downvote']
            )

            return HttpResponseRedirect(reverse("main"))

    form = addPost()

    return render(request, html, {'form': form})
