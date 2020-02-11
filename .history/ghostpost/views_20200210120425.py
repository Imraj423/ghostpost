from ghostpost.models import ghostPost



def index(request):
    item = ghostPost.objects.all()
    return render(request, 'index.html', {'data': item})

