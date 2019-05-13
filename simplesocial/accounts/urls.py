from django.conf.urls import url
from django.contrib.auth.views import LoginView,LogoutView
from . import views

app_name='accounts'  #What is this? why is it required??
urlpatterns=[
    url(r'^login/$',LoginView.as_view(template_name='login.html'),name='login'),
    url(r'^logout/$',LogoutView.as_view(),name='logout'),
    url(r'^signup/$',views.SignUp.as_view(),name='signup'),

]
