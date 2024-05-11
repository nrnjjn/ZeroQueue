from django.conf.urls import url
from working_hours import  views

urlpatterns = [
    url('^view_hours',views.view_hours),
    url('^hours',views.hours),
    url('^up/(?P<idd>\w+)',views.update,name='up')

]