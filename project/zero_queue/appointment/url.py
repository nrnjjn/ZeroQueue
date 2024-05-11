from django.conf.urls import url
from appointment import views
urlpatterns = [
   url('^appo/',views.appo),
   url('^cancel/',views.cancel),
   url('^view/',views.view),
    url('^status/',views.status),
    url('^ cncl/(?P<idd>\w+)',views.cncl,name='cncl'),
url('^ aprv/(?P<idd>\w+)',views.aprv,name='abcd'),
url('^ rejct/(?P<idd>\w+)',views.reject,name='efg'),

]