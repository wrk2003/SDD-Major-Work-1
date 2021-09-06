from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('staircase', views.staircase, name="staircase"),
    path('sam-and-substrings', views.sam, name="sam"),
    path('morgan-and-a-string', views.morgan, name="morgan")
]