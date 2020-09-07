from django.conf.urls import url

import views

urlpatterns = [
    url("", views.home, name="home"),
    url("add", views.add, name="add")
]
