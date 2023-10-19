from django.urls import path
from . import views

app_name = 'haircut'

urlpatterns = [
    path('', views.index, name='index')
]
