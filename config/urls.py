"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from main.views import indexView,todoDeleteView,todoDoneView,todoCreateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path("index/", indexView, name="index"),
    path("done/<int:id>/", todoDoneView, name="done"),
    path("delete/<int:id>/", todoDeleteView, name="delete"),
    path("create/", todoCreateView, name="create"),
]
