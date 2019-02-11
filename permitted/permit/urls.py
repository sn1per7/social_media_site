from django.conf.urls import url
from django.urls import path
from . import views

app_name = "permit"

urlpatterns = [
    path('', views.UserLogView.as_view(), name="login"),
    #path('homepage', views.Homepage.as_view(), name="homepage"),
    url('^profile/(?P<person_id>[0-9a-z]+)/$', views.Homepage.as_view(), name="homepage"),
    url('^message/(?P<person_id>[0-9a-z]+)/$', views.Messages.as_view(), name="messages"),
    path('register', views.UserRegView.as_view(), name="register"),
    path('logout', views.LogoutView.as_view(), name="logout"),
]