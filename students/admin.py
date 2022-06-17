from django.contrib import admin
from students.models import * 
# Register your models here.
admin.site.register(Student)  
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Faculty)
 # Register your models here.    This is required by admin.register().           