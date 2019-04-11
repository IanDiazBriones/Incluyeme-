from . import views
from django.urls import path, include # new
urlpatterns = [
	path('signup', views.SignUp.as_view(), name='signup'),
]
