import datetime

from django.shortcuts import render,redirect
from .models import loans
from django.contrib.auth.decorators import login_required
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
    return redirect('loan_view')

@login_required
def delete(request,pk):
    l=loans.objects.filter(pk=int(pk)).first()
    if(not l.lender):
        l.delete()

    return redirect('loan_dashboard')

@login_required
def modify(request,pk):
    l=loans.objects.filter(pk=int(pk)).first()
    if request.method == "POST":
            l.amt = request.POST['amt']
            l.tenure = request.POST['tenure']
            l.interest = request.POST['interest']
            l.save()

            return redirect('loan_dashboard')
    else:
            return render(request, 'loans/modify_loan.html')


    return redirect('loan_dashboard')


# def loan_detail_view(request,id):
#     loan=loans.objects.filter()