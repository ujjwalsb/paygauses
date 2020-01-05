from django.conf.urls import url
from lendingEnquiry import views



urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^thankyou$', views.thankyou, name='thankyou'),
]


# handler404 = 'lendingEnquiry.views.handler404'
# handler500 = 'lendingEnquiry.views.handler500'