"""APIDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from post import views as postViews
from category import views as categoryViews
from author import views as authorViews
from .router import router
from rest_framework.response import Response

urlpatterns = [
    path('admin/', admin.site.urls),
    path('post', postViews.list),
    path('post/<int:pk>', postViews.detail),
    path('category', categoryViews.list),
    path('category/<int:pk>', categoryViews.detail),
    path('author', authorViews.list),
    path('author/<int:pk>', authorViews.detail),
    path('api/', include(router.urls))
]
def error404():
    response = {"message":"trang khong ton tai"}
    return Response(response)

handler404 = error404()

