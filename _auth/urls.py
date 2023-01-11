from django.urls import path
from _auth.views import CompanyView, AuthenticationView, AuthenticationVerificationView, UserView, CompanyDetailView


urlpatterns = [
    path("user/", UserView.as_view()),
    path("v1/auth/", AuthenticationView.as_view()),
    path("v1/auth/verification/", AuthenticationVerificationView.as_view()),
    path("company/", CompanyView.as_view()),
    path("company/<int:pk>", CompanyDetailView.as_view()),
]