from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.
class loans(models.Model):
    #applicant=models.OneToOneField(User,on_delete=models.CASCADE,related_name='applicant_user')
    applicant=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    lender=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True,related_name='lender_user')
    applied_date=models.DateTimeField(default=datetime.now)
    accepted_date=models.DateTimeField(null=True,blank=True)
    status=models.BooleanField(default=False)
    amt=models.IntegerField()
    tenure=models.IntegerField()
    interest=models.DecimalField(decimal_places=2,max_digits=4)

    def __str__(self):
        return f"{self.applicant}'s demand of RS {self.amt}"

    # def save(self,*args,**kwargs):
    #     super().save(*args,**kwargs)