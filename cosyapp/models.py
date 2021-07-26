from django.db import models
from django.db.models import Model

# Create your models here.
class Project(models.Model):
    # owner = models.ForeignKey(User,verbose_name='User',related_name='project')
    title = models.CharField(max_length=100)
    series = models.CharField(max_length=100)
    due_date = models.DateField()
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    completed = models.BooleanField(default=False)
    photo = models.ImageField(default=None, upload_to='uploads/')

    # need to create relationship with User class?

    def __str__(self):
        return self.title

class Part(models.Model):
    name = models.CharField(max_length=100)
    project = models.ForeignKey(Project,verbose_name='Project',related_name='part',on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Task(models.Model):
    description = models.CharField(max_length=150)
    completed = models.BooleanField(default=False)
    part = models.ForeignKey(Part,verbose_name='Part',related_name='task',on_delete=models.CASCADE)

    def __str__(self):
        return self.description

# from django.contrib.auth.models import  User, Group
# class Portfolio(models.Model):
#  owner = models.ForeignKey(User,verbose_name = 'User',related_name='portfolios')
#  company = models.TextField(null=True)
#  volume = models.IntegerField(blank=True)
#  date = models.DateField(null=True)
#  isin = models.TextField(null=True)
