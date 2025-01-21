from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', views.random, name="random")
    path('admin/', admin.site.urls),
]