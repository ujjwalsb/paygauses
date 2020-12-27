from django.urls import path
from .views import loanEnquiry
from .views import homeDesignEnquiry
from .views import constructionEnquiry
from .views import eventManagementEnquiry
from .views import thankyou
urlpatterns = [
    path('', loanEnquiry, name='loanEnquiry'),
    path('homeDesignEnquiry', homeDesignEnquiry, name='homeDesignEnquiry'),
    path('constructionEnquiry', constructionEnquiry, name='constructionEnquiry'),
    path('eventManagementEnquiry', eventManagementEnquiry, name='eventManagementEnquiry'),
    path('thankyou', thankyou, name='thankyou')
]

# handler404 = 'lendingEnquiry.views.handler404'
# handler500 = 'lendingEnquiry.views.handler500'
