from django.contrib import admin
from .models import LoanEnquiry

class PayModelAdmin(admin.ModelAdmin):
    list_display = ["firstName", "email", "mobile", "loanAmount", "loanNeedTime"]
    list_display_links = ["firstName", "email", "mobile", "loanAmount", "loanNeedTime"]
    #list_editable = ["link"]
    list_filter = ["loanNeedTime", "revenue", "registeredAs", "ageOfBusiness"]
    search_fields = ["firstName", "lastName", "email", "mobile"]

    class Meta:
        model = LoanEnquiry


admin.site.register(LoanEnquiry, PayModelAdmin)
