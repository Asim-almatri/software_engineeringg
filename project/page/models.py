from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    country = models.CharField(max_length=50)
    grade = models.CharField(max_length=5)
    courses = models.ManyToManyField('Course', related_name='students', blank=True)
    photo = models.ImageField(upload_to='students/', blank=True, null=True)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20)
    hours = models.PositiveIntegerField()
    instructor = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    specialization = models.CharField(max_length=100)
    years_of_experience = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
