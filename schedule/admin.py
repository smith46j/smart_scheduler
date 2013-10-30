from django.contrib import admin
from .models import Employee, Shift, AvailableShift, Position, PositionRequirements, DailyRequirements, Schedule


admin.site.register(Employee)
admin.site.register(Shift)
admin.site.register(AvailableShift)
admin.site.register(Position)
admin.site.register(PositionRequirements),
admin.site.register(DailyRequirements),
admin.site.register(Schedule),
