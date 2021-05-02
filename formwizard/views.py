from django.http import HttpResponseRedirect
from formtools.wizard.views import SessionWizardView
from .forms import *

form_list = [SignupForm1, SignupForm2]

class SignUpWizard(SessionWizardView):
    template_name = 'wizardform.html'  
    def done(self, form_list, **kwargs):
        return HttpResponseRedirect('/')
        
            
        

