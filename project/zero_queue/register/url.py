from django.conf.urls import url
from register import views

urlpatterns = [
    # url('register',views.register),
    url('user',views.user)

]