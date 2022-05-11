import datetime
import os
from django.shortcuts import render,redirect
from .models import loans
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
@login_required
def loan_view(request):
    loan=loans.objects.all()
    l=[]

    for i in loan:
        if i.applicant!=request.user and (not i.status):
            l.append(i)
    context={'loans':l}

    return render(request,'loans/loan_view.html',context)
@login_required
def apply_loan(request):
    cibil = request.user.bank_profile.CIBIL
    max = 0

    if (cibil > 700):
        max = 10000000
    elif (cibil > 650):
        max = 6000000
    elif cibil > 600:
        max = 3000000
    elif cibil > 550:
        max = 1000000
    elif cibil > 500:
        max = 100000
    elif cibil > 450:
        max = 50000
    else:
        max = 10000

    if request.method=="POST":
        applicant=request.user
        amt=request.POST['amt']
        if int(amt)<=max:

            tenure=request.POST['tenure']
            interest=request.POST['interest']
            loan=loans(applicant=applicant,amt=amt,tenure=tenure,interest=interest)
            loan.save()
            message = "Loan of id=" + str(loan.pk) + " applied successfully of\namount:" + str(loan.amt) + "\ntenure:" + str(loan.tenure) + "\ninterest:" + str(loan.interest)+"\nYou will receive mail once any client accepts the loan"
            send_message("Loan Applied!", message, loan.applicant.email)
            return redirect('loan_dashboard')

    return render(request,'loans/apply_loan.html',{'max':max})

@login_required
def loan_dashboard(request):
    context={'applied':loans.objects.filter(applicant=request.user),'accepted':loans.objects.filter(lender=request.user)}

    return render(request,'loans/loan_dashboard.html',context)
@login_required
def accept(request,pk):
    l=loans.objects.filter(pk=int(pk)).first()
    l.lender=request.user
    l.accepted_date=datetime.datetime.now()
    l.status=True
    l.save()
    message="Dear "+str(l.applicant)+", your loan with id:"+str(l.id)+"and amount:" +str(l.amt)+"has been accepted by "+str(l.lender)
    send_message("Loan accepted!", message, l.applicant.email)
    message="You have successfully accepted loan with id"+str(l.id)+"and amount:"+str(l.amt)
    send_message("loan processed successfully!",message,l.lender.email)

    return redirect('loan_view')

@login_required
def delete(request,pk):
    l=loans.objects.filter(pk=int(pk)).first()
    if(not l.lender):
        email=l.applicant.email
        amt=l.amt
        l.delete()
        send_message("Loan updated successfully","Loan of amount:"+str(amt)+" deleted successfully",email)

    return redirect('loan_dashboard')

@login_required
def modify(request,pk):
    l=loans.objects.filter(pk=int(pk)).first()
    if request.method == "POST":
            l.amt = request.POST['amt']
            l.tenure = request.POST['tenure']
            l.interest = request.POST['interest']
            l.save()
            print(settings.EMAIL_HOST_USER,settings.EMAIL_HOST_PASSWORD)
            message="Loan with id="+str(l.pk)+" updated successfully \namount:"+str(l.amt)+"\ntenure:"+str(l.tenure)+"\ninterest:"+str(l.interest)
            send_message("Loan updated successfully",message,l.applicant.email)

            return redirect('loan_dashboard')
    else:
            return render(request, 'loans/modify_loan.html')


def send_message(subject,message,to):
    send_mail(subject,message,"loanhuntservices@gmail.com",[to],fail_silently=False)

# send_message("test mail","this is test mail","shivam23gopchade@gmail.com")