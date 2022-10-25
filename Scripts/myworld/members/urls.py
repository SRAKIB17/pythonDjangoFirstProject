from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('all/', views.members, name='name'),
    path('add/', views.add, name='add'),
    path('add/add_record/', views.add_record, name='add_record'),
    path('delete/<int:id>', views.delete_record, name='delete record'),
    path('update/<int:id>', views.update, name='update record'),
    path('update/update_record/<int:id>/',
         views.update_record, name='update record'),
    path('template/', views.template_test, name='name')
]
