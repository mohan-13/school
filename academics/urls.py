from django.conf.urls import url ,include
from . import views

urlpatterns=[
    url(r'^marks/',views.marks)
]