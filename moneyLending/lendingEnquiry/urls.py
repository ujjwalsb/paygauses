from django.urls import path
from .views import loanEnquiry
from .views import homeDesignEnquiry
from .views import constructionEnquiry
# from .views import eventManagementEnquiry
from .views import servicesAt99Enquiry
from .views import thankyou, vehicleServiceEnquiry, rentalServiceEnquiry, investmentServiceEnquiry
urlpatterns = [
    path('', loanEnquiry, name='loanEnquiry'),
    path('homeDesignEnquiry', homeDesignEnquiry, name='homeDesignEnquiry'),
    path('constructionEnquiry', constructionEnquiry, name='constructionEnquiry'),
    # path('eventManagementEnquiry', eventManagementEnquiry, name='eventManagementEnquiry'),
    path('servicesAt99Enquiry', servicesAt99Enquiry, name='servicesAt99Enquiry'),
    path('vehicleServiceEnquiry', vehicleServiceEnquiry, name='vehicleServiceEnquiry'),
    path('rentalServiceEnquiry', rentalServiceEnquiry, name='rentalServiceEnquiry'),
    path('investmentServiceEnquiry', investmentServiceEnquiry, name='investmentServiceEnquiry'),
    path('thankyou', thankyou, name='thankyou')
]

# handler404 = 'lendingEnquiry.views.handler404'
# handler500 = 'lendingEnquiry.views.handler500'
