from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from loans.models import loans
from .models import request_loan
from datetime import datetime
# Create your views here.
@login_required
def modify_request(request,pk):
    if request.method == "POST":
            tenure = request.POST['tenure']
            interest = request.POST['interest']
            loan_req=request_loan(loan_pk=int(pk),request=request.user,tenure=tenure,interest=interest)
            loan_req.save()

            return redirect('loan_view')
    else:
            return render(request, 'req_loan/modify_loan.html')

def modify_request_view(request,pk):
    loan=loans.objects.filter(pk=int(pk)).first()
    req=request_loan.objects.filter(loan_pk=int(pk))
    context={'loan':loan,'req':req}

    return render(request,'req_loan/modify_loan_view.html',context)

def accept_modify(request,pk):
    req = request_loan.objects.filter(pk=int(pk)).first()
    l=loans.objects.filter(pk=int(req.loan_pk)).first()
    l.tenure=req.tenure
    l.interest=req.interest
    l.status=True
    l.accepted_date=datetime.now()
    l.lender=req.request
    l.save()

    return redirect('loan_dashboard')
