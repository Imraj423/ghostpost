"""ghostpost URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from ghostpost.models import ghostPost

admin.site.register(ghostPost)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('detail/', views.detail),
    path('addpost/', views.post_add),
    path('like/<int:id>', views.like, name="index"),
    path('dislike/<int:id>', views.dislike, name="index")
    ]
