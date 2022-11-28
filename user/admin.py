from django.contrib import admin

from .models import Student, Course, Mentor, Language

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Language)
admin.site.register(Mentor)

