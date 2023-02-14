from django.urls import path
from orders.views import ApplicationFormView, AdminApplicationFormView


urlpatterns = [
    path("application/<int:pk>", ApplicationFormView.as_view()),
    path("admin/applications", AdminApplicationFormView.as_view())
]