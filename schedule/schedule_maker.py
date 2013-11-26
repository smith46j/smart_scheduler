from .models import *
from datetime import datetime
class generate_schedule(object):
    current_schdule = []
    attempted_schedule = []

    def generate_schdule(self):
        #This is where all of the work happens.
        #First get the start time,
        #To make this easier we will break it into parts of the day, 
        #to do this we will find requirements at good intervals 

        try:
            schedule = Schedule.objects.get(date=datetime.now())
        except:
            print "Nothing Here"

        #If nothing in the schedule for the day then no requirements split day up
        #into 8 hour shifts and make a schedule for that so 12am to 8am and so on
        if schedule.requirements:
            generate_for_normalized(AvailableShift.objects.filter(
                datetime.now()))

        return self.current_schdule

    
    def generate_for_normalized(self, query_set):
        for shift in query_set:
            self.current_schdule.add(shift)
        







        

