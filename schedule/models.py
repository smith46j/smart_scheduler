from django.db import models

class Employee(models.Model):
    class Meta:
        ordering = ['last_name']

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    min_hours = models.IntegerField()
    max_hours = models.IntegerField()
    target_hours = models.IntegerField()
    position = models.ManyToManyField('Position')

    def __unicode__(self):
        return u'{first} {last}'.format(first=self.first_name, last=self.last_name)

class Shift(models.Model):
    class Meta:
        ordering = ['date']

    employee = models.ForeignKey('Employee')
    time_start = models.TimeField()
    time_end = models.TimeField()
    date = models.DateField()

    def __unicode__(self):
        return u'{date} -- {employee}'.format(date=self.date, employee=self.employee)

class AvailableShift(models.Model):
    class Meta:
        ordering = ['date']

    employee = models.ForeignKey('Employee')
    time_start = models.TimeField()
    time_end = models.TimeField()
    date = models.DateField()

    def __unicode__(self):
        return u'{date} -- {employee}'.format(date=self.date, employee=self.employee)

class Position(models.Model):
    class Meta:
        ordering = ['name']

    name = models.CharField(max_length=50)

    def __unicode__(self):
        return unicode(self.name)

class PositionRequirements(models.Model):
    class Meta:
        ordering = ''
        verbose_name_plural = 'Position Requirements'

    position = models.ForeignKey('Position')
    min_employees = models.IntegerField()
    max_employees = models.IntegerField()

    def __unicode__(self):
        return u'{pos} {min} {max}'.format(pos=self.position, min=self.min_employees, max=self.max_employees)

class DailyRequirements(models.Model):
    class Meta:
        ordering = ''
        verbose_name_plural = 'Daily Requirements'

    day_start = models.TimeField()
    day_end = models.TimeField()
    position_req = models.ForeignKey('PositionRequirements')

    def __unicode__(self):
        return u'{pk} - {posreq}'.format(pk=self.pk, posreq=self.position_req)

class Schedule(models.Model):
    class Meta:
        ordering = ['date']

    date = models.DateField()
    requirements = models.ManyToManyField('DailyRequirements')

    def __unicode__(self):
        return u'{date} {req}'.format(date=self.date, req=self.requirements)
