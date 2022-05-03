from accounts import views

from django.urls import path
from django.views.generic import TemplateView

app_name = 'accounts'

urlpatterns = [
    path('my-profile/', views.MyProfile.as_view(), name='my_profile'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('confirm/', TemplateView.as_view(template_name="confirm.html"), name='confirm'),
]
