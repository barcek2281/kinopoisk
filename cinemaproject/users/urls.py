from django.urls import path, include
from .views import Register
from users import views


urlpatterns = [
    path('', include('django.contrib.auth.urls')),
	path('profile', views.profile_page, name='profile'),
    path('register/', Register.as_view(), name='register'),
]
