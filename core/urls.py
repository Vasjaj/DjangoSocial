from django.urls import path
from django.conf.urls import include, url
from core import views


app_name = 'core'
urlpatterns = [
    url('profile/', views.profile, name="profile"),
]
