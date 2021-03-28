from django.db import models

class LoanEnquiry(models.Model):
    firstName = models.CharField(max_length=100, null=True, unique=False)
    lastName = models.CharField(max_length=100, null=True, unique=False)
    email = models.CharField(max_length=100, null=True, unique=False)
    mobile = models.CharField(max_length=100, null=True, unique=False)
    loanAmount = models.CharField(max_length=100, null=True, unique=False)
    loanNeedTime = models.CharField(max_length=100, null=True, unique=False)
    revenue = models.CharField(max_length=100, null=True, unique=False)
    ageOfBusiness = models.CharField(max_length=100, null=True, unique=False)
    registeredAs = models.CharField(max_length=100, null=True, unique=False)

    def __str__(self):
        return self.mobile

    class Meta:
        verbose_name_plural = "Loan Enquiry Management"


class HomeDesignEnquiry(models.Model):
    firstName = models.CharField(max_length=100, null=True, unique=False)
    lastName = models.CharField(max_length=100, null=True, unique=False)
    email = models.CharField(max_length=100, null=True, unique=False)
    mobile = models.CharField(max_length=100, null=True, unique=False)
    home_design_enquiry_service = models.CharField(max_length=100, null=True, unique=False)

    def __str__(self):
        return self.mobile

    class Meta:
        verbose_name_plural = "Home Design Enquiry Management"


class ConstructionEnquiry(models.Model):
    firstName = models.CharField(max_length=100, null=True, unique=False)
    lastName = models.CharField(max_length=100, null=True, unique=False)
    email = models.CharField(max_length=100, null=True, unique=False)
    mobile = models.CharField(max_length=100, null=True, unique=False)
    construction_enquiry_service = models.CharField(max_length=100, null=True, unique=False)

    def __str__(self):
        return self.mobile

    class Meta:
        verbose_name_plural = "Construction Enquiry Management"

class ServicesAt99Enquiry(models.Model):
    firstName = models.CharField(max_length=100, null=True, unique=False)
    lastName = models.CharField(max_length=100, null=True, unique=False)
    email = models.CharField(max_length=100, null=True, unique=False)
    mobile = models.CharField(max_length=100, null=True, unique=False)
    servicesAt99_enquiry_service = models.CharField(max_length=100, null=True, unique=False)

    def __str__(self):
        return self.mobile

    class Meta:
        verbose_name_plural = "Services at rupees 99 Enquiry Management"

#VehicleServiceEnquiry
class VehicleServiceEnquiry(models.Model):
    firstName = models.CharField(max_length=100, null=True, unique=False)
    lastName = models.CharField(max_length=100, null=True, unique=False)
    email = models.CharField(max_length=100, null=True, unique=False)
    mobile = models.CharField(max_length=100, null=True, unique=False)
    vehicle_enquiry_service = models.CharField(max_length=100, null=True, unique=False)

    def __str__(self):
        return self.mobile

    class Meta:
        verbose_name_plural = "Vehicle Enquiry Management"

class RentalServiceEnquiry(models.Model):
    firstName = models.CharField(max_length=100, null=True, unique=False)
    lastName = models.CharField(max_length=100, null=True, unique=False)
    email = models.CharField(max_length=100, null=True, unique=False)
    mobile = models.CharField(max_length=100, null=True, unique=False)
    rental_enquiry_service = models.CharField(max_length=100, null=True, unique=False)

    def __str__(self):
        return self.mobile

    class Meta:
        verbose_name_plural = "Rental Enquiry Management"

class InvestmentServiceEnquiry(models.Model):
    firstName = models.CharField(max_length=100, null=True, unique=False)
    lastName = models.CharField(max_length=100, null=True, unique=False)
    email = models.CharField(max_length=100, null=True, unique=False)
    mobile = models.CharField(max_length=100, null=True, unique=False)
    investment_enquiry_service = models.CharField(max_length=100, null=True, unique=False)

    def __str__(self):
        return self.mobile

    class Meta:
        verbose_name_plural = "Investment Enquiry Management"


# class EventManagementEnquiry(models.Model):
#     firstName = models.CharField(max_length=100, null=True, unique=False)
#     lastName = models.CharField(max_length=100, null=True, unique=False)
#     email = models.CharField(max_length=100, null=True, unique=False)
#     mobile = models.CharField(max_length=100, null=True, unique=False)
#     loanAmount = models.CharField(max_length=100, null=True, unique=False)
#     loanNeedTime = models.CharField(max_length=100, null=True, unique=False)
#     revenue = models.CharField(max_length=100, null=True, unique=False)
#     ageOfBusiness = models.CharField(max_length=100, null=True, unique=False)
#     registeredAs = models.CharField(max_length=100, null=True, unique=False)
#
#     def __str__(self):
#         return self.mobile
#
#     class Meta:
#         verbose_name_plural = "Event Enquiry Management"


class ProductOrServiceEnquiry(models.Model):
    firstName = models.CharField(max_length=100, null=True, unique=False)
    lastName = models.CharField(max_length=100, null=True, unique=False)
    email = models.CharField(max_length=100, null=True, unique=False)
    mobile = models.CharField(max_length=100, null=True, unique=False)
    loanAmount = models.CharField(max_length=100, null=True, unique=False)
    loanNeedTime = models.CharField(max_length=100, null=True, unique=False)
    revenue = models.CharField(max_length=100, null=True, unique=False)
    ageOfBusiness = models.CharField(max_length=100, null=True, unique=False)
    registeredAs = models.CharField(max_length=100, null=True, unique=False)

    def __str__(self):
        return self.mobile

    class Meta:
        verbose_name_plural = "Product or Service Enquiry Management"
