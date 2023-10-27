from django.db import models


# Create your models here.
# company model
class Company(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=50)
    about = models.TextField()
    type = models.CharField(max_length=100, choices=(('IT', 'it'), ('Non IT', 'Non it')))
    started_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


# Employee model
class Employee(models.Model):
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=12)
    address = models.CharField(max_length=50)
    designation = models.CharField(max_length=20, choices=(('Manager', 'manager'), ('Developer', 'developer')))
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
