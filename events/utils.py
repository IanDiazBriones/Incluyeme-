from calendar import HTMLCalendar
from datetime import datetime as dtime, date, time
import datetime
from .models import Event
from users.models import Pasaje
 
class EventCalendar(HTMLCalendar):
    def __init__(self, events=None):
        super(EventCalendar, self).__init__()
        self.events = events
 
    def formatday(self, day, weekday, events, request):

        user= request.user
        Pasajes = Pasaje.objects.all()
        events_from_day = events.filter(Fecha_Salida__day=day)
        events_html = "<ul>"
        for event in events_from_day:
            for Evento in Pasajes:
                if Evento.Dueño == user:
                    events_html += str(Evento.Hora_Salida) + "<br>"
                    events_html += str(Evento.Destino) + "<br>"
        events_html += "</ul>"
 
        if day == 0:
            return '<td class="noday">&nbsp;</td>'  # day outside month
        else:
            return '<td class="%s">%d%s</td>' % (self.cssclasses[weekday], day, events_html)
 
    def formatweek(self, theweek, events, request):

        s = ''.join(self.formatday(d, wd, events, request) for (d, wd) in theweek)
        return '<tr>%s</tr>' % s
 
    def formatmonth(self, theyear, themonth, request, withyear=True):

        user= request.user
        events = Pasaje.objects.filter(Fecha_Salida__month=themonth).filter(Dueño__exact=user)

        v = []
        a = v.append
        a('<div style="overflow-x:auto;">')
        a('\n')
        a('<table border="0" cellpadding="0" cellspacing="0" class="month">')
        a('\n')
        a(self.formatmonthname(theyear, themonth, withyear=withyear))
        a('\n')
        a(self.formatweekheader())
        a('\n')
        for week in self.monthdays2calendar(theyear, themonth):
            a(self.formatweek(week, events, request))
            a('\n')
        a('</table>')
        a('\n')
        return ''.join(v) 