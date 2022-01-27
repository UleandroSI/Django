from django.urls import path
from simplemooc.core import views
from . import views

urlpatterns = [

    path('', views.home, name='home'),
]
