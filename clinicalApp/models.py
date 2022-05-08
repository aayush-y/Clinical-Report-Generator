
from django.db import models

# Create your models here.
class patient(models.Model):
    firstName=models.CharField(max_length=30)
    lastName=models.CharField(max_length=30)
    age=models.IntegerField()

class clinicalData(models.Model):
    componentChoices=[('hw','Height/Weight'),('bp','Blood Pressure'),('heartrate','Heart Rate')]
    componentName=models.CharField(choices=componentChoices,max_length=20)
    componentValue=models.CharField(max_length=20)
    registeredDate=models.DateTimeField(auto_now_add=True)
    Patient=models.ForeignKey(patient,on_delete=models.CASCADE)