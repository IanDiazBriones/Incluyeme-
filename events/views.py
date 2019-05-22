from __future__ import unicode_literals

from django.shortcuts import render
from .models import Event
import datetime
import calendar
from django.urls import reverse, reverse_lazy
from calendar import HTMLCalendar
from django.utils.safestring import mark_safe
from .utils import EventCalendar
from users.models import CustomUser
# Create your views here.


def CalendarView(request):
	after_day= request.GET.get('date', None)
	context= None or {}

	if not after_day:
		d = datetime.date.today()
	else:
		try:
			split_after_day = after_day.split('-')
			d = datetime.date(year=int(split_after_day[0]), month=int(split_after_day[1]), day=1)
		except:
			d = datetime.date.today()
	previous_month = datetime.date(year=d.year, month=d.month, day=1)  # find first day of current month
	previous_month = previous_month - datetime.timedelta(days=1)  # backs up a single day
	previous_month = datetime.date(year=previous_month.year, month=previous_month.month,
															day=1)  # find first day of previous month
	
	last_day = calendar.monthrange(d.year, d.month)
	next_month = datetime.date(year=d.year, month=d.month, day=last_day[1])  # find last day of current month
	next_month = next_month + datetime.timedelta(days=1)  # forward a single day
	next_month = datetime.date(year=next_month.year, month=next_month.month,
													day=1)  # find first day of next month


	cal = EventCalendar()
	html_calendar = cal.formatmonth(d.year, d.month, request, withyear=True)
	html_calendar = html_calendar.replace('<td ', '<td  width="150" height="150"')
	context['calendar'] = mark_safe(html_calendar)
	context['previous_month'] = 'date=' + str(previous_month.year) + '-' + str(previous_month.month)
	context['next_month'] = 'date=' + str(next_month.year) + '-' + str(next_month.month)

	return render(request, 'events/calendar.html', context)