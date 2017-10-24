from django.contrib import admin
from .models import student
from .models import course
from .models import subject
from .models import marks
from .models import teacher, teaches
# Register your models here.
admin.site.register(student)
admin.site.register(course)
admin.site.register(subject)
admin.site.register(marks)
admin.site.register(teacher)
admin.site.register(teaches)