from django.conf.urls import url
from temp import views

urlpatterns=[
    url('^index/',views.index),
    url('^admin/',views.admin),
    url('^organisation/',views.organisation),
    url('^user/',views.user),
]