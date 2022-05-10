from django.shortcuts import render,redirect
import BankProfile.forms as forms
from django.contrib.auth.decorators import login_required
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
            print("form saved")
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