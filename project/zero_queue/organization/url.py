from django.conf.urls import url
from organization import views

urlpatterns = [
    url('^register/',views.register),
    url('^organisation/',views.organisation),
    url('^org/',views.org),
    url('^search/',views.search),
    url('^aprv/(?P<idd>\w+)',views.aprove,name='apv'),
    url('^rejct/(?P<idd>\w+)',views.reject,name='rejct')

]