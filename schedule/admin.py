from django.contrib import admin
from .models import Employee, Shift, AvailableShift, Position, PositionRequirements, DailyRequirements, Schedule

class EmployeeAdmin(admin.ModelAdmin):
    ordering = ('last_name', 'first_name')
    search_fields = ['last_name', 'first_name', 'position']
    list_display = (
            'last_name',
            'first_name',
            'min_hours',
            'max_hours',
            'target_hours',
            )
    list_filter = ('position',)

class ShiftAdmin(admin.ModelAdmin):
    ordering = ('date',)
    search_fields = ['employee', 'date']
    list_display = (
            'employee',
            'date',
            'time_start',
            'time_end',
            )
    list_filter = ('employee',)

class AvailableShiftAdmin(admin.ModelAdmin):
    ordering = ('employee',)
    search_fields = ['employee', 'date']
    list_display = (
            'employee',
            'date',
            'time_start',
            'time_end',
            )
    list_filter = ('employee',)

class PositionAdmin(admin.ModelAdmin):
    ordering = ('name',)
    search_fields = ('name',)
    list_display = ('name',)

class PositionRequirementsAdmin(admin.ModelAdmin):
    ordering = ('position',)
    search_fields = ('position',)
    list_display = ('position', 'min_employees', 'max_employees',)
    list_filter = ('position',)

class DailyRequirementsAdmin(admin.ModelAdmin):
    ordering = ('day_start',)
    search_fields = ('day_start', 'day_end',)
    list_display = ('day_start', 'day_end', 'position_req',)
    list_filter = ('day_start', 'day_end',)

class ScheduleAdmin(admin.ModelAdmin):
    ordering = ('date',)
    search_fields = ('date',)
    list_display = ('date',)

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Shift, ShiftAdmin)
admin.site.register(AvailableShift, AvailableShiftAdmin)
admin.site.register(Position, PositionAdmin)
admin.site.register(PositionRequirements, PositionRequirementsAdmin)
admin.site.register(DailyRequirements, DailyRequirementsAdmin)
admin.site.register(Schedule, ScheduleAdmin)
