from .models import Shift, AvailableShift, Schedule
import datetime


class generate_schedule(object):
    current_schdule = []
    attempted_schedule = []

    def generate_for_normalized(self, query_set):
        for aval_shift in query_set:
            shift = self.make_shift(aval_shift)
            self.current_schdule.append(shift)

    def generate_schdule(self):
        """This is where all of the work happens.
        First get the start time,
        To make this easier we will break it into parts of the day,
        to do this we will find requirements at good intervals"""
        schedule = None

        try:
            schedule = Schedule.objects.get(date=datetime.datetime.now())
        except:
            print "Nothing Here"
        if schedule.requirements:
            self.generate_for_normalized(AvailableShift.objects.filter(
                date = datetime.date.today()))

        return self.current_schdule

    def make_shift(self, aval_shift):
        shift = Shift(employee = aval_shift.employee,
                          time_start = aval_shift.time_start,
                          time_end = aval_shift.time_end,
                          date = aval_shift.date)
        shift.save()
        return aval_shift
