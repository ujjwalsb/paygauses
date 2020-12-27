from django.shortcuts import render
from .models import HomeDesignEnquiry


def loanEnquiry(request):
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
        enquiry = loanEnquiry.objects.create(
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
    return render(request, 'loanEnquiry.html', {})

def homeDesignEnquiry(request):
    return render()

def homeDesignEnquiry(request):
    firstName = request.GET.get("firstName")
    lastName = request.GET.get("lastName")
    email = request.GET.get("email")
    mobile = request.GET.get("mobile")
    home_design_enquiry_service = request.GET.get("home_design_enquiry_service")

    if firstName:
        enquiry = HomeDesignEnquiry.objects.create(
            firstName=firstName,
            lastName=lastName,
            email=email,
            mobile=mobile,
            home_design_enquiry_service = home_design_enquiry_service
        )

        return render(request, 'thankyou.html', {})
    return render(request, 'homeDesignEnquiry.html', {})


def constructionEnquiry(request):
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
    return render(request, 'constructionEnquiry.html', {})


def eventManagementEnquiry(request):
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
    return render(request, 'eventManagementEnquiry.html', {})


def thankyou(request):
    return render(request, 'thankyou.html', {})
