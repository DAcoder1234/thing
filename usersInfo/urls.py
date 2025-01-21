from django.urls import path
from . import views
#urls
urlpatterns = [
    path('', views.random, name='random'),
	path('convert/', views.convert, name='convert')
]