"""
This should generate the schedule.

This assumes that the user will put in enough available shifts

"""
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

        positions = self.get_postions(requirements)
        for aval_shift in query_set.order_by('time_start', 'employee__target_hours'):
            add = True
            if (len(set(aval_shift.employee.position.all()).intersection(positions)) != 0):
                add = self.check_if_need_to_add(requirements, aval_shift)

            if add and self.check_employee_time(aval_shift):
                shift = self.make_shift(aval_shift)
                self.current_schdule.append(shift)

    def generate_schdule(self):
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
            self.generate_for_normalized(
                AvailableShift.objects.filter(date=datetime.date.today()),
                schedule.requirements)
        return self.current_schdule

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
    def get_postions(cls, requirements):
        """
        Get all the positions from the requirements.

        This is where we get all the positions for the requirements
        Return the positions in an array

        """

        postions = []
        for requirement in requirements.all():
            postions.append(requirement.position_req.position)
        return postions

    def check_if_need_to_add(self, requirements, aval_shift):
        """
        Return a boolean if we should add the shift to the schedule.

        We will check for each requirement for the time if it matches with the
        aval shift, then we will find if we have already meet this req with the
        current schedule.

        """
        for req in requirements.all():
            if req.day_start < aval_shift.time_start and req.day_end > aval_shift.time_start:
                counter = 0
                for shift in self.current_schdule:
                    if req.day_start < shift.time_start and req.day_end > shift.time_end:
                        counter += 1
                if counter < req.position_req.max_employees:
                    return True
                else:
                    return False

    def check_employee_time(self, aval_shift):
        """ Return a true if below max hours for employee."""
        print "HERE"
        dict_of_emplpoyee_and_hours = {}
        name = aval_shift.employee.first_name + aval_shift.employee.last_name
        for shift in self.current_schdule:
            if (shift.employee.first_name + shift.employee.last_name) == name:
                if name in dict_of_emplpoyee_and_hours:
                    dict_of_emplpoyee_and_hours[name] += int(shift.time_end - shift.time_start)
                else:
                    dict_of_emplpoyee_and_hours[name] = int(shift.time_end - shift.time_start)
        if name not in dict_of_emplpoyee_and_hours:
            return True
        if dict_of_emplpoyee_and_hours[name] >= aval_shift.employee.target_hours:
            return False
        else:
            return True
