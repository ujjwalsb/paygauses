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
        verbose_name_plural = "Paygauses Information Management"


class HomeDesignEnquiry(models.Model):
    firstName = models.CharField(max_length=100, null=True, unique=False)
    lastName = models.CharField(max_length=100, null=True, unique=False)
    email = models.CharField(max_length=100, null=True, unique=False)
    mobile = models.CharField(max_length=100, null=True, unique=False)
    home_design_enquiry_service = models.CharField(max_length=100, null=True, unique=False)

    def __str__(self):
        return self.mobile

    class Meta:
        verbose_name_plural = "Paygauses Information Management"


class ConstructionEnquiry(models.Model):
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
        verbose_name_plural = "Paygauses Information Management"


class EventManagementEnquiry(models.Model):
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
        verbose_name_plural = "Paygauses Information Management"


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
        verbose_name_plural = "Paygauses Information Management"
