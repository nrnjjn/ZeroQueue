from django.conf.urls import url
from complaints import views

urlpatterns = [
    url('^complaints/',views.complaints),
    url('^post/(?P<idd>\w+)',views.post,name='rply')

]