
from django.urls import path, include
from users import views as users_views

urlpatterns = [
    path('register/', users_views.register, name="register"),
]
