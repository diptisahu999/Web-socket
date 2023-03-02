from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=23)
    email=models.EmailField()
    password=models.CharField(max_length=32)
    mobile=models.CharField(max_length=34)

    def __str__(self):
        return self.mobile
    
    class Meta:
        db_table='student_table'


class Job(models.Model):
    job=models.ForeignKey(Student,on_delete=models.CASCADE)
    salary=models.CharField(max_length=34)

    def __str__(self):
        return self.salary
