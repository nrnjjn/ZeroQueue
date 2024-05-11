from django.conf.urls import url
from department import views

urlpatterns = [
    url('department/',views.department),
    url('search/',views.search_dept),
]
