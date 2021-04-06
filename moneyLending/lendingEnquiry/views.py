from django.shortcuts import render
from django.views.decorators.http import require_GET, require_POST
from .models import HomeDesignEnquiry
from .models import LoanEnquiry
from .models import ConstructionEnquiry, VehicleServiceEnquiry, RentalServiceEnquiry, ServicesAt99Enquiry


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
        enquiry = LoanEnquiry.objects.create(
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
    construction_enquiry_service = request.GET.get("construction_enquiry_service")

    if firstName:
        enquiry = ConstructionEnquiry.objects.create(
            firstName=firstName,
            lastName=lastName,
            email=email,
            mobile=mobile,
            construction_enquiry_service=construction_enquiry_service
        )

        return render(request, 'thankyou.html', {})
    return render(request, 'constructionEnquiry.html', {})

def servicesAt99Enquiry(request):
    firstName = request.GET.get("firstName")
    lastName = request.GET.get("lastName")
    email = request.GET.get("email")
    mobile = request.GET.get("mobile")
    servicesAt99_enquiry_service = request.GET.get("servicesAt99_enquiry_service")

    if firstName:
        enquiry = ServicesAt99Enquiry.objects.create(
            firstName=firstName,
            lastName=lastName,
            email=email,
            mobile=mobile,
            servicesAt99_enquiry_service=servicesAt99_enquiry_service
        )

        return render(request, 'thankyou.html', {})
    return render(request, 'servicesAt99Enquiry.html', {})

# def eventManagementEnquiry(request):
#     firstName = request.GET.get("firstName")
#     lastName = request.GET.get("lastName")
#     email = request.GET.get("email")
#     mobile = request.GET.get("mobile")
#     loanAmount = request.GET.get("loanAmount")
#     loanNeedTime = request.GET.get("loanNeedTime")
#     revenue = request.GET.get("revenue")
#     ageOfBusiness = request.GET.get("ageOfBusiness")
#     registeredAs = request.GET.get("registeredAs")
#
#     if firstName:
#         enquiry = paygausesEnquiry.objects.create(
#             firstName=firstName,
#             lastName=lastName,
#             email=email,
#             mobile=mobile,
#             loanAmount=loanAmount,
#             loanNeedTime=loanNeedTime,
#             revenue=revenue,
#             ageOfBusiness=ageOfBusiness,
#             registeredAs=registeredAs,
#         )
#
#         return render(request, 'thankyou.html', {})
#     return render(request, 'eventManagementEnquiry.html', {})

#VehicleServiceEnquiry
def vehicleServiceEnquiry(request):
    firstName = request.GET.get("firstName")
    lastName = request.GET.get("lastName")
    email = request.GET.get("email")
    mobile = request.GET.get("mobile")
    vehicle_enquiry_service = request.GET.get("vehicle_enquiry_service")

    if firstName:
        enquiry = VehicleServiceEnquiry.objects.create(
            firstName=firstName,
            lastName=lastName,
            email=email,
            mobile=mobile,
            vehicle_enquiry_service=vehicle_enquiry_service
        )

        return render(request, 'thankyou.html', {})
    return render(request, 'vehicle_enquiry_service.html', {})

def rentalServiceEnquiry(request):
    firstName = request.GET.get("firstName")
    lastName = request.GET.get("lastName")
    email = request.GET.get("email")
    mobile = request.GET.get("mobile")
    rental_enquiry_service = request.GET.get("rental_enquiry_service")

    if firstName:
        enquiry = RentalServiceEnquiry.objects.create(
            firstName=firstName,
            lastName=lastName,
            email=email,
            mobile=mobile,
            rental_enquiry_service=rental_enquiry_service
        )

        return render(request, 'thankyou.html', {})
    return render(request, 'rental_enquiry_service.html', {})

def investmentServiceEnquiry(request):
    firstName = request.GET.get("firstName")
    lastName = request.GET.get("lastName")
    email = request.GET.get("email")
    mobile = request.GET.get("mobile")
    investment_enquiry_service = request.GET.get("investment_enquiry_service")

    if firstName:
        enquiry = InvestmentServiceEnquiry.objects.create(
            firstName=firstName,
            lastName=lastName,
            email=email,
            mobile=mobile,
            investment_enquiry_service=investment_enquiry_service
        )

        return render(request, 'thankyou.html', {})
    return render(request, 'investment_enquiry_service.html', {})

def thankyou(request):
    return render(request, 'thankyou.html', {})
