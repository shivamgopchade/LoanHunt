from django.shortcuts import render,redirect
import user.forms as forms
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from datetime import datetime
# Create your views here.
def register(request):
    if request.method=='POST':
        form = forms.UserRegisterForm(request.POST)
        #is_sign_in=request.POST['sign in']
        #if 'sign in'
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            email=form.cleaned_data.get('email')
            send_message("Welcome to LoanHunt fam!","Hi "+str(username)+",Welcome to the LoanHunt family where C2C loan becomes simple!!\n"
                                                                        "Please update your BANK PROFILE asap.This will increase your CIBIL score for more benefits!!\n"
                                                                        "Also you can update your profile anytime by visiting USER PROFILE.\nThankyou for trusting us!!",email)
            #messages.success(request,f'account created sucessfully for {username}.Please Login')
            return redirect('login')
        else:
            #username=request.POST['username']
            #messages.warning(request,f'Something went wrong please try Again {username}')
            return redirect('register')
    else:
        form=forms.UserRegisterForm()
    return render(request,'users/register.html',{'form':form})

@login_required
def UpdateProfile(request):
    if request.method == 'POST':
        u_form = forms.UserUpdateForm(request.POST, instance=request.user)
        p_form = forms.ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            form = u_form
            send_message("User profile updated successfully!","Your user profile updated on:"+str(datetime.now()),request.user.email)
            return redirect('home')
    else:
        u_form = forms.UserUpdateForm(instance=request.user)
        p_form = forms.ProfileUpdateForm(instance=request.user.profile)

        context = {'u_form': u_form, 'p_form': p_form}

        return render(request, 'users/UpdateProfile.html', context)

def send_message(subject,message,to):
    send_mail(subject,message,"loanhuntservices@gmail.com",[to],fail_silently=False)