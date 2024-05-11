from django.conf.urls import url
from appoinment_token import views
urlpatterns = [
    url('token',views.token)
]