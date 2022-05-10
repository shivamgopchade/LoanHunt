from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.

class request_loan(models.Model):
    loan_pk=models.IntegerField()
    request=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    asked_date=models.DateTimeField(default=datetime.now)
    accepted=models.BooleanField(default=False)
    tenure = models.IntegerField()
    interest = models.DecimalField(decimal_places=2, max_digits=4)

    def __str__(self):
        return f"{self.request}'s request to loan id: {self.loan_pk}"