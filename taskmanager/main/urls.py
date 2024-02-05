
from django.urls import path
from . import views


urlpatterns = [
    path('',views.index, name='ind'),
    path('news',views.news, name='nw'),
    path('about',views.about, name='ab'),
]
