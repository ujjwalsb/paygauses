
from django.shortcuts import render
from .models import paygausesEnquiry


def home(request):
    firstName = request.GET.get("firstName")
    lastName = request.GET.get("lastName")
    email = request.GET.get("email")
    mobile = request.GET.get("mobile")
    loanAmount = request.GET.get("loanAmount")
    loanNeedTime = request.GET.get("loanNeedTime")
    revenue = request.GET.get("revenue")
    ageOfBusiness = request.GET.get("ageOfBusiness")
    registeredAs = request.GET.get("registeredAs")

    if firstName:
        enquiry = paygausesEnquiry.objects.create(
                                            firstName=firstName,
                                            lastName=lastName,
                                            email=email,
                                            mobile=mobile,
                                            loanAmount=loanAmount,
                                            loanNeedTime=loanNeedTime,
                                            revenue=revenue,
                                            ageOfBusiness=ageOfBusiness,
                                            registeredAs=registeredAs,
                                            )
    
        return render(request, 'thankyou.html', {})
    return render(request, 'home.html', {})

def thankyou(request):
    return render(request, 'thankyou.html', {})
