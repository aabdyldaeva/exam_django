import datetime
from django.db import models

class Language(models.Model):
    name = models.CharField(max_length=100)
    month_to_learn = models.IntegerField()

    def __str__(self):
        return f'Язык: {self.name} Продолжительность в мес: {self.month_to_learn}'

class AbstractPerson(models.Model):
    name = models.CharField(max_length=50,default = 0)
    email = models.CharField(unique=True,max_length = 200, default = 0)
    phone_number = models.IntegerField(default = 0)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

class Student(AbstractPerson):
    OPER_SYS = (
        ('windows','WINDOWS'),
        ('macOS', 'MAC'),
        ('linux', 'LINUX'),
    )
    work_study_place = models.CharField(max_length=100, null=True)
    has_own_notebook = models.BooleanField(help_text='Есть ли свой ноутбук?')
    preferred_os = models.CharField(max_length=10, choices=OPER_SYS)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Имя: {self.name} '

class Mentor(AbstractPerson):
    main_work = models.CharField(max_length=100, null=True)
    experience = models.DateField()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Имя: {self.name} '


class Course(models.Model):
    name = models.CharField(max_length=50)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    date_started = models.DateField()
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)

    # def get_end_date(self):
    #     course_length = Language.month_to_learn
    #     current_date_month = datetime.now().month
    #     return days_course_length - current_date





