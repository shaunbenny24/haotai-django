from django.urls import path,include
from . import views

urlpatterns = [
    path ('', views.index, name = 'home'),
    path ('about/', views.about , name ='about'),
    path ('jobss/', views.jobs ,name = 'emp'),
    path ('jobss/<int:id>', views.jobs ,name = 'job'),
    path ('jobsingle/<int:id>', views.jobsingle ,name= 'jobsingle'),
    path ('options/', views.options ),
]