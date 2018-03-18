from django.conf.urls import include, url
from registration import views

urlpatterns = [
    url('signup/', views.signup, name='signup'),
]
