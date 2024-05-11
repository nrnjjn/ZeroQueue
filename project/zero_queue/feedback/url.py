from django.conf.urls import url
from feedback import views

urlpatterns = [
    url('feedback',views.feedback),
    url('view',views.view)

]