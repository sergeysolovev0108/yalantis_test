from django.db import models


class Course(models.Model):
    name = models.CharField(verbose_name='Название курса', max_length=128,)
    start_date = models.DateField(verbose_name='Дата начала курса', )
    end_date = models.DateField(verbose_name='Дата окончания курса', )
    number_of_lectures = models.IntegerField(verbose_name='Количество лекций', )
