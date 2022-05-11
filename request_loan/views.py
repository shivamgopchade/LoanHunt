from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from loans.models import loans
from .models import request_loan
from datetime import datetime
from django.core.mail import send_mail

@login_required
def modify_request(request,pk):
    if request.method == "POST":
            tenure = request.POST['tenure']
            interest = request.POST['interest']
            loan = loans.objects.filter(pk=int(pk)).first()
            loan_req=request_loan(loan_pk=int(pk),request=request.user,tenure=tenure,interest=interest)
            loan_req.save()
            message = "Dear " + str(loan.applicant) + ", your loan with id:" + str(loan.id)+" got a new request.Following are details:\n" \
                                                                                            "client:"+str(request.user)+"\n Tenure:"+str(tenure)+"\n Interest:"+str(interest)
            #send_message("Your Loan Got a request!", message, loan.applicant.email)
            message = "You added a modification card with id:" + str(loan_req.id)
            #send_message("Request send successfully!", message, loan_req.request.email)
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

    message = "Dear " + str(l.applicant) + ", your loan with id:" + str(l.id) + " and amount:" + str(
        l.amt) + " has been accepted by " + str(l.lender)
    #send_message("Loan accepted!", message, l.applicant.email)
    message = "You have successfully accepted loan with id" + str(l.id) + " and amount:" + str(l.amt)
    #send_message("loan processed successfully!", message, l.lender.email)

    return redirect('loan_dashboard')

def send_message(subject,message,to):
    send_mail(subject,message,"loanhuntservices@gmail.com",[to],fail_silently=False)