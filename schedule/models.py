from django.db import models

class Employee(models.Model):
    class Meta:
        ordering = ['last_name']

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    min_hours = models.IntegerField()
    max_hours = models.IntegerField()
    target_hours = models.IntegerField()
    position = models.ForeignKey('Position')

class Shift(models.Model):
    class Meta:
        ordering = ['date']

    employee = models.ForeignKey('Employee')
    time_start = models.TimeField()
    time_end = models.TimeField()
    date = models.DateField()

class AvailableShift(models.Model):
    class Meta:
        ordering = ['date']

    employee = models.ForeignKey('Employee')
    time_start = models.TimeField()
    time_end = models.TimeField()
    date = models.DateField()

class Position(models.Model):
    class Meta:
        ordering = ['name']

    name = models.CharField(max_length=50)

class PositionRequirements(models.Model):
    class Meta:
        ordering = ''

    postion = models.ForeignKey('Position')
    min_employees = models.IntegerField()
    max_employees = models.IntegerField()

class DailyRequirements(models.Model):
    class Meta:
        ordering = ''

    day_start = models.TimeField()
    day_end = models.TimeField()
    position_req = models.ForeignKey('PositionRequirements')

class Schedule(models.Model):
    class Meta:
        ordering = 'date'

    date = models.DateField()
    requirements = models.ForeignKey('DailyRequirements')

