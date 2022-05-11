import decimal
from django.core.mail import send_mail
from django.shortcuts import render,redirect
import BankProfile.forms as forms
from django.contrib.auth.decorators import login_required
from .models import bank_profile as bank_profile_model
# Create your views here.
def dashboard(request):
    return render(request,'profile/dashboard.html')

@login_required
def bank_profile(request):
    if request.method == 'POST':
        form = forms.BankProfileform(request.POST,request.FILES,instance=request.user.bank_profile)
        #print(form.user)
        if form.is_valid():
            form.save()
            bp=bank_profile_model.objects.filter(user=request.user).first()
            val = ((-1*bp.DUE * (0.3)) + (bp.CUR *(0.25)) +(bp.Credit_duration * 0.25) + bp.CTC * 0.2)/900
            #print(val)
            bp.CIBIL=val
            bp.save()
            #send_message("Bank Profile Updated!","your bank profile has been updated successfully!!",bp.user.email)
            #print("form saved")
            # messages.success(request,f'account created sucessfully for {username}.Please Login')
            return redirect('home')
        else:
            print(form.errors)
            # username=request.POST['username']
            # messages.warning(request,f'Something went wrong please try Again {username}')
            return redirect('bank_profile')
    else:
        form = forms.BankProfileform(instance=request.user.bank_profile)    
    return render(request, 'bankform.html', {'form': form})

def send_message(subject,message,to):
    send_mail(subject,message,"loanhuntservices@gmail.com",[to],fail_silently=False)