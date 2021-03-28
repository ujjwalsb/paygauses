from django.contrib import admin
from .models import LoanEnquiry, HomeDesignEnquiry, ConstructionEnquiry, ServicesAt99Enquiry, VehicleServiceEnquiry, RentalServiceEnquiry, InvestmentServiceEnquiry


class LoanEnquiryModel(admin.ModelAdmin):
    list_display = ["firstName", "email", "mobile", "loanAmount", "loanNeedTime"]
    list_display_links = ["firstName", "email", "mobile", "loanAmount", "loanNeedTime"]
    # list_editable = ["link"]
    list_filter = ["loanNeedTime", "revenue", "registeredAs", "ageOfBusiness"]
    search_fields = ["firstName", "lastName", "email", "mobile"]

    class Meta:
        model = LoanEnquiry


class HomeDesignEnquiryModel(admin.ModelAdmin):
    list_display = ["firstName", "email", "mobile", "home_design_enquiry_service"]
    list_display_links = ["firstName", "email", "mobile", "home_design_enquiry_service"]
    # list_editable = ["link"]
    list_filter = ["home_design_enquiry_service"]
    search_fields = ["firstName", "lastName", "email", "mobile"]

    class Meta:
        model = HomeDesignEnquiry


class ConstructionEnquiryModel(admin.ModelAdmin):
    list_display = ["firstName", "email", "mobile", "construction_enquiry_service"]
    list_display_links = ["firstName", "email", "mobile", "construction_enquiry_service"]
    # list_editable = ["link"]
    list_filter = ["construction_enquiry_service"]
    search_fields = ["firstName", "lastName", "email", "mobile"]

    class Meta:
        model = ConstructionEnquiry

class ServicesAt99EnquiryModel(admin.ModelAdmin):
    list_display = ["firstName", "email", "mobile", "servicesAt99_enquiry_service"]
    list_display_links = ["firstName", "email", "mobile", "servicesAt99_enquiry_service"]
    # list_editable = ["link"]
    list_filter = ["servicesAt99_enquiry_service"]
    search_fields = ["firstName", "lastName", "email", "mobile"]

    class Meta:
        model = ServicesAt99Enquiry

class VehicleServiceEnquiryModel(admin.ModelAdmin):
    list_display = ["firstName", "email", "mobile", "vehicle_enquiry_service"]
    list_display_links = ["firstName", "email", "mobile", "vehicle_enquiry_service"]
    # list_editable = ["link"]
    list_filter = ["vehicle_enquiry_service"]
    search_fields = ["firstName", "lastName", "email", "mobile"]

    class Meta:
        model = VehicleServiceEnquiry


class RentalServiceEnquiryModel(admin.ModelAdmin):
    list_display = ["firstName", "email", "mobile", "rental_enquiry_service"]
    list_display_links = ["firstName", "email", "mobile", "rental_enquiry_service"]
    # list_editable = ["link"]
    list_filter = ["rental_enquiry_service"]
    search_fields = ["firstName", "lastName", "email", "mobile"]

    class Meta:
        model = RentalServiceEnquiry

class InvestmentServiceEnquiryModel(admin.ModelAdmin):
    list_display = ["firstName", "email", "mobile", "investment_enquiry_service"]
    list_display_links = ["firstName", "email", "mobile", "investment_enquiry_service"]
    # list_editable = ["link"]
    list_filter = ["investment_enquiry_service"]
    search_fields = ["firstName", "lastName", "email", "mobile"]

    class Meta:
        model = InvestmentServiceEnquiry


admin.site.register(LoanEnquiry, LoanEnquiryModel)
admin.site.register(HomeDesignEnquiry, HomeDesignEnquiryModel)
admin.site.register(ConstructionEnquiry, ConstructionEnquiryModel)
admin.site.register(ServicesAt99Enquiry, ServicesAt99EnquiryModel)
admin.site.register(VehicleServiceEnquiry, VehicleServiceEnquiryModel)
admin.site.register(RentalServiceEnquiry, RentalServiceEnquiryModel)
admin.site.register(InvestmentServiceEnquiry, InvestmentServiceEnquiryModel)
