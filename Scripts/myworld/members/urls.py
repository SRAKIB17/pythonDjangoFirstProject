from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('all/', views.members, name='name'),
    path('add/', views.add, name='add'),
    path('add/add_record/', views.add_record, name='add_record'),
    # path('hello/', views.html_view, name='name')
]
