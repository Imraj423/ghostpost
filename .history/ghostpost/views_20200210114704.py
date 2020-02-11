from ghostpost.models import ghostPost
from django.shortcuts import render
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
            Forms.objects.create(
                title=data['title'],
                description=data['description'],
                author=data['author'],
                instructions=data['instructions']
            )

            return HttpResponseRedirect(reverse("main"))

    form = addPost()

    return render(request, html, {'form': form})
