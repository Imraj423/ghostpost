from ghostpost.models import ghostPost
from django.contrib import messages


def index(request):
    item = ghostPost.objects.all()
    return render(request, 'ghostpost/index.html', {'data': item})
