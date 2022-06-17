from django.db import models

# Create your models here.
from django.db import models
# from django.db.models.base import Model

# Create your models here.
class Faculty(models.Model):
    faculty_name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.faculty_name
    


class Department(models.Model):
    department_name = models.CharField(max_length=30)
    faculty_id = models.ForeignKey(Faculty, on_delete = models.CASCADE)

    def __str__(self):
        return self.department_name
    

class Course(models.Model):
    course_name = models.CharField(max_length=40)
    fees = models.DecimalField(max_digits=8, decimal_places=2)
    credit = models.IntegerField()
    department_id = models.ForeignKey(Department, on_delete = models.CASCADE)

    def __str__(self):
        return self.course_name
    

class Student(models.Model):
    names = models.CharField(max_length=80)
    gender = models.CharField(max_length=6)
    dob = models.DateField()
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return self.names
    
    


