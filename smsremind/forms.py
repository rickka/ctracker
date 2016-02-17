from django import forms
from django.forms import widgets
from django.forms import extras
from .models import *
from django.core import validators
from choices import *


class ContractForm(forms.Form):
    contract_title = forms.CharField(required=True)
    client_name = forms.CharField(required=True)
    client_contact = forms.CharField(required=True, max_length=13)
    
    dmark_owner = forms.ChoiceField(choices=EMPLOYEES, required=True)

    date_signed = forms.DateField(widget=extras.SelectDateWidget(years=range(2012, datetime.date.today().year+10)))
    date_expiry = forms.DateField(widget=extras.SelectDateWidget)

    #dmark_contact = forms.CharField()
    #dmark_email = forms.EmailField()
    #set_alert   = forms.ChoiceField(choices=SET)

    def clean_dmark_owner(self):
	owner = self.cleaned_data["dmark_owner"]

        print owner[0]
	if len(owner) <= 1:
	    raise forms.ValidationError("This field is needed")
	return owner
    
    def clean_client_contact(self):
	contact = self.cleaned_data["client_contact"]
        
        if len(contact) < 9 or len(contact) > 13:
	    raise forms.ValidationError("Enter Valid Phone number")
	return contact


def must_be_empty(value):#validators must always take a value(thats in the field)
    if value:
        raise forms.ValidationError('is not empty')

class JobForm(forms.Form):
    jobname = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form'}))
    deadline = forms.DateField(widget=extras.SelectDateWidget)
    email = forms.EmailField()
    verify_email = forms.EmailField(help_text="Please verify your email address")
    suggestion = forms.CharField(widget=forms.Textarea)##added
    #setter = forms.CharField()
    honeypot = forms.CharField(required=False,
                               widget=forms.HiddenInput,
                               label="Leave empty",
                               #validators=[validators.MaxLengthValidator(0)])
				validators=[must_be_empty])#name of validator function defined

    def clean(self):
        cleaned_data = super().clean()
	email = cleaned_data.get('email')
	verify = cleaned_data.get('verify_email')

	if email != verify:
	    raise forms.ValidationError(
		"You need to enter same email in both fields")


    '''
    #overriding default clean method, django searches for <clean_fieldname> method 
    def clean_honeypot(self):
        honeypot = self.cleaned_data['honeypot']
        if len(honeypot):
	    raise forms.ValidationError(
		"honeypot should be left empty. Bad bot!")
	return honeypot
    '''


'''
OWNERS = (('',''),
          ('josh', 'Josh'),
          ('steve', 'Steve'),
          ('kennedy','Kennedy'),
          ('joseph','Joseph'),
          ('sylvia','Sylvia'),
          ('andrew','Andrew'),
          ('micheal', 'Micheal'),
          ('kitamirike','Kitamirike'),
          ('joy','Joy'),
          ('floriante','Floriante'),
          ('patrick', 'Patrick'),
)


class ReminderForm(forms.Form):
    
    job = forms.ModelChoiceField(queryset=Job.objects.all().order_by('name'))
    owner = forms.ChoiceField(choices=OWNERS)
    contact = forms.CharField()
'''



    











