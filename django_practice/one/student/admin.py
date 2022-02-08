from typing import Counter
from django.contrib import admin
from student.models import *

# Register your models here.
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Dept)
admin.site.register(course)
admin.site.register(Marks)
admin.site.register(Teacher)