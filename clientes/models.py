from django.db import models

# Create your models here.

class Cliente(models.Model):
    name = models.CharField(max_length = 150)
    lastName = models.CharField(max_length = 150)
    document = models.BigIntegerField(null = False, blank = False, primary_key=True)
    birthdate = models.DateField(null = False, blank = False)
    email = models.CharField(max_length = 250)
    country = models.CharField(max_length = 50)
    city = models.CharField(max_length = 50)
    income = models.FloatField(null = False, blank = False)
    debt = models.FloatField(null = False, blank = False)
    economicActivity = models.CharField(max_length = 150)
    company = models.CharField(max_length = 100)
    profession = models.CharField(max_length = 150)
    
        
    def __str__(self):
        return f"{self.document} {self.name} {self.email} {self.income} {self.debt}"
