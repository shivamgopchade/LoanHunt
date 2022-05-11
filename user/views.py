from django.shortcuts import render,redirect
import user.forms as forms
from django.contrib.auth.decorators import login_required
# Create your views here.
def register(request):
    if request.method=='POST':
        form = forms.UserRegisterForm(request.POST)
        #is_sign_in=request.POST['sign in']
        #if 'sign in'
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
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
            return redirect('home')
    else:
        u_form = forms.UserUpdateForm(instance=request.user)
        p_form = forms.ProfileUpdateForm(instance=request.user.profile)

        context = {'u_form': u_form, 'p_form': p_form}

        return render(request, 'users/UpdateProfile.html', context)