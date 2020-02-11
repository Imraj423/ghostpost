from ghostpost.models import ghostPost
from django.shortcuts import render


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
                description=data['description'],
                author=data['author'],
                instructions=data['instructions']
            )

            return HttpResponseRedirect(reverse("main"))

    form = addRecipe()

    return render(request, html, {'form': form})
