from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.db.models import Model
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    series = models.CharField(max_length=100)
    due_date = models.DateField()
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    completed = models.BooleanField(default=False)
    photo = models.ImageField(default=None, blank=True, upload_to='uploads/')
    owner = models.ForeignKey(User, related_name='project', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Part(models.Model):
    name = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Task(models.Model):
    description = models.CharField(max_length=150)
    completed = models.BooleanField(default=False)
    part = models.ForeignKey(Part, on_delete=models.CASCADE)

    def __str__(self):
        return self.description

class ToBuyItem(models.Model):
    description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    link = models.URLField(max_length=200, blank=True)
    completed = models.BooleanField(default=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.description

class ReferencePhoto(models.Model):
    photo = models.ImageField(default=None, blank=True, upload_to='uploads/')
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.description
