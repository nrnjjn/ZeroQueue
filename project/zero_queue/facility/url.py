from django.conf.urls import url
from facility import views

urlpatterns = [
    url('facility',views.facility),
    url('view',views.view)

]