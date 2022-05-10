from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class bank_profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    Aadhar = models.FileField(upload_to='Aadhar/',null=True)
    Pan = models.FileField(upload_to='Pan/',null=True)
    Salary = models.FileField(upload_to='Salary/',null=True)
    Bank=models.CharField(max_length=30,null=True)
    CTC=models.IntegerField(null=True)
    #user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    #info = models.CharField(max_length=50, label='Tell Something about yourself',blank=True)
    def __str__(self):
        return f"{self.user} bank profile"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('home')


