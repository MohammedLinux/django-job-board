from operator import mod
from pyexpat import model
from turtle import title
from django.db import models

# Create your models here.
JOB_TYPE = (
    ('Full Time', 'Full Time'),
    ('Part Time','Part Time'),
)
class Job(models.Model):
    title = models.CharField(max_length=100) #column
    job_type = models.CharField(max_length=15,choices=JOB_TYPE)
    desc = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    Vacncy = models.IntegerField(default=1)
    salary = models.BigIntegerField(default=0)
    experaince = models.IntegerField(default=1)

    def __str__(self) -> str:
        return self.title


    