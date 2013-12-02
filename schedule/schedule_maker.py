from .models import Shift, AvailableShift, Schedule
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
import datetime


class Generate_Schedule(object):

    """The class we use to generate a schedule from requirements."""

    current_schdule = []
    attempted_schedule = []

    def generate_for_normalized(self, query_set, requirements):
        """
        Generate a schedule from the earilest avalaible shift.

        This is where we will start with the earliest available shifts and
        check if there are any requirements and then make the shifts and
        add them to current schdule

        """

        postions = self.get_postions(requirements)
        for aval_shift in query_set:
            if aval_shift.emplpoyee.position in positions:
                #TODO: need to figure out if this is met.
            shift = self.make_shift(aval_shift)
            self.current_schdule.append(shift)

    @classmethod
    def generate_schdule(cls):
        """
        Method to call to generate a schedule.

        This is where all of the work happens
        First get the start time,
        To make this easier we will break it into parts of the day,
        to do this we will find requirements at good intervals
        This will return the list of shifts that were created

        """
        schedule = None

        try:
            schedule = Schedule.objects.get(date=datetime.datetime.now())
        except MultipleObjectsReturned:
            print "Nothing Here"
        except ObjectDoesNotExist:
            print "Nothing Here"

        if schedule.requirements:
            cls.generate_for_normalized(AvailableShift.objects.filter(
                date=datetime.date.today()), schedule.requirements)
        return cls.current_schdule

    @classmethod
    def make_shift(cls, aval_shift):
        """
        Make the shifts.

        Returns a shift

        """
        shift = Shift(employee=aval_shift.employee,
                      time_start=aval_shift.time_start,
                      time_end=aval_shift.time_end,
                      date=aval_shift.date)
        shift.save()
        return shift

    @classmethod
    def get_postions(self, requirements):
        """
        Get all the positions from the requirements.

        This is where we get all the positions for the requirements

        """

        postions = []
        for requirement in requirements:
            postions.append(requirement.postion)
        return postions
