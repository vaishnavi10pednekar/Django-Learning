
from django.urls import path, include
from firstprojectt import views

urlpatterns = [
    path('', views.home, name="home"),
    path('task/', views.task, name="task"),
    path('aboutus/', views.aboutus, name="aboutus"),
    path('contactus/', views.contactus, name="contactus"),
    path('address/', views.address, name= "address"),
]
