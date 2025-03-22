from django.urls import path
from .views import get_user, login_user, register_user, update_user, logout_user

urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('user/', get_user, name='get_user'),
    path('user/', update_user, name='update_user'),
]