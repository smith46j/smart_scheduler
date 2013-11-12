# Create your views here.

### Only View should be the calender. 
from django.views.generic import TemplateView
from .models import Shift 
from datetime import date, timedelta

class CalendarTemplateView(TemplateView):
    """
        This will display all of the shifts for the week starting with today
        It will also accept a get request variable of a date(mm/dd/yyyy format)
        This will allow us to start at that day
    """

    template_name = 'calendar_view.html'

    def get_context_data(self, **kwargs):
        context = super(CalendarTemplateView, self).get_context_data(**kwargs)
        context['all_shifts_today'] = Shift.objects.filter(date = date.today())
        context['all_shifts_tom'] = Shift.objects.filter(
                date = (date.today() + timedelta(days = 1)))
        context['all_shifts_2'] = Shift.objects.filter(
                date = (date.today() + timedelta(days = 2)))
        context['all_shifts_3'] = Shift.objects.filter(
                date = (date.today() + timedelta(days = 3)))
        context['all_shifts_4'] = Shift.objects.filter(
                date = (date.today() + timedelta(days = 4)))
        context['all_shifts_5'] = Shift.objects.filter(
                date = (date.today() + timedelta(days = 5)))
        context['all_shifts_6'] = Shift.objects.filter(
                date = (date.today() + timedelta(days = 6)))
        return context
