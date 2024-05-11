from django.conf.urls import url
from cancellation import views

urlpatterns = [
    url('^cancel/',views.cancel )

]