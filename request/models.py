from django.db import models
from django.urls import reverse

# Create your models here.

class attendance(models.Model):
    student_name=models.CharField(max_length=300)
    student_class=models.CharField(max_length=100)
    requbranch=models.CharField(max_length=10)
    reason=models.CharField(max_length=1000)
    start_date=models.DateField()
    end_date=models.DateField()
    isapproved=models.BooleanField(default= False )

    def get_absolute_url(self):
        return ('/request')

    def __str__(self):
        return self.student_name + " :" + self.reason