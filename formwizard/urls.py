from django.urls import path
from .views import SignUpWizard,form_list

app_name = 'formwizard'

urlpatterns = [
    path('', SignUpWizard.as_view(form_list), name='home'),
]