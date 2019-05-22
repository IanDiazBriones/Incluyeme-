from . import views
from django.urls import path, include # new

app_name = 'events'
urlpatterns = [
	path('calendar/', views.CalendarView, name='calendar'),
]


