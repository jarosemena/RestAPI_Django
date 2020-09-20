from django.conf.urls import patterns, url 
import views 

urlpatterns = patterns ( 
    '',
    url(r'^soap_service/', views.my_soap_application),
)