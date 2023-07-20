from django.db import models
from django.contrib.auth.models import User


class Person(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200,null=False,blank=False)
    last_name = models.CharField(max_length=200,null=True,blank=True)
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
class Candidate(models.Model):

    person = models.ForeignKey(Person,on_delete=models.CASCADE)
    roll_number = models.CharField(max_length=300,null=True,blank=True)
    mathMarks = models.CharField(max_length=100,null=True,blank=True)
    computerMarks = models.CharField(max_length=100,null=True,blank=True)
    resoningMarks = models.CharField(max_length=100,null=True,blank=True)
    englishMarks = models.CharField(max_length=100,null=True,blank=True)