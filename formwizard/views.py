from django.http import HttpResponseRedirect
from formtools.wizard.views import SessionWizardView
from .forms import *
from .models import  *

form_list = [SignupForm1, SignupForm2]

class SignUpWizard(SessionWizardView):
    template_name = 'wizardform.html'

    instance = None

    def get_form_instance( self, step ):
        if self.instance is None:
            self.instance = SignUp()
        return self.instance

    def done(self, form_list, **kwargs):
        self.instance.save()
        return HttpResponseRedirect('/')
        
            
        

