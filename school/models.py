from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    date_birth = models.DateField()
    email = models.EmailField(unique=True, blank=True, max_length=30)
    cpf = models.CharField(max_length=11, unique=True)
    phone_number = models.CharField(max_length=14, blank=True, null=True)

    def __str__(self):
        return self.name
    

class Course(models.Model):
    level_choices = [
        ('B', 'Beginner'),
        ('I', 'Intermediate'),
        ('A', 'Advanced'),
    ]

    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=10, unique=True)    
    description = models.TextField(max_length=100, blank=False)
    start_date = models.DateField()
    end_date = models.DateField()
    level = models.CharField(max_length=50, blank=False, null=False, default='B' ,choices=level_choices)

    def __str__(self):
        return self.code
    
