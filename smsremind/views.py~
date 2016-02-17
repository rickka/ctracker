from django.shortcuts import render, render_to_response, get_object_or_404
from .models import *
from django.contrib import messages
from django import forms
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse, reverse_lazy
from .forms import ContractForm

#added imports

from django.contrib import messages
from django.core.mail import send_mail


def add_job(request):

    if request.method == "POST":
        form = JobForm(request.POST)

        if form.is_valid():

            send_mail(
	        'Suggestion from {}'.format(form.cleaned_data['jobname']), #first argument of method is email subject
 		form.cleaned_data['suggestion'],
		'{jobname} <{deadline}>'.format(**form.cleaned_data),  #feed format method a dict and it'll use the dict keys to to fill in the placeholders
		['patrifire@yahoo.com'] # recipient
            )
            print "sending mail"

	    messages.add_message(request, messages.SUCCESS, 'Thanks for your Suggestion!')

	    return HttpResponseRedirect(reverse('job_form'))
	return render(request, 'add_job.html', {'form': form})


'''
            print form
            job_name = form.cleaned_data["jobname"]
            dead_line = form.cleaned_data["deadline"]
            #print job_name
            #print dead_line            

            try:
                newjob = Job.objects.create(name=job_name, deadline=dead_line)
                return HttpResponseRedirect(reverse_lazy('add_job'))

            except Exception as e:
                messages.error(request, str(e))
                
    else:
        form = JobForm()
        return render(request, 'index.html', {'form': form})
'''

def add_contract(request):

    form = ContractForm()
    if request.method == "POST":
	print request.method
        form = ContractForm(request.POST)

        if form.is_valid():
	    ctitle     = form.cleaned_data["contract_title"]
            cl_name    = form.cleaned_data["client_name"]
            cl_contact = form.cleaned_data["client_contact"]
            d_owner    = form.cleaned_data["dmark_owner"]
            date_sign  = form.cleaned_data["date_signed"]
            date_exp   = form.cleaned_data["date_expiry"]

	    try:
		print "entered try"
		contract = Contract.objects.create(title=ctitle, signed=date_sign, expiry=date_exp, clname=cl_name,clcontact=cl_contact, dname=d_owner)

		reminder = Reminder.objects.create(contract=contract, is_set=True)

                
		print "saving........"

	        messages.add_message(request, messages.SUCCESS, 'Contract "%s" has been saved!' % ctitle)

	    except Exception as e:
		messages.add_message(request, messages.INFO, str(e))

        else:  #if form is not valid
	    print "form is not valid"
	    for field in form.errors:
		print field

	    return render_to_response('contractform.html', {'ctc_form':form}, context_instance=RequestContext(request))


    #else: #request.method == "GET"
    #   form = ContractForm()
    #    ctx = {'ctc_form' : form}
    #    return render_to_response('contractform.html', ctx,context_instance=RequestContext(request))
        
    return render(request, 'contractform.html', {'ctc_form': form})
    #return HttpResponseRedirect(reverse('contractform'))



def contractlist(request):
    
    contracts = Contract.objects.all()
    if 'searchq' in request.GET:
        contracts = contracts.filter(title__contains=request.GET['searchq'])

    contracts = contracts.order_by('-created')
    #for contract in contracts:
    #	print contract.dname

    ctcs = {'ctcs': contracts}

    print "reaching dict"
    return render_to_response('contractlist.html', ctcs, context_instance=RequestContext(request))


'''
def clientlist(request):
    clients = Client.objects.all()
    if 'searchq' in request.GET:
	clients = clients.filter(name__contains=request.GET['searchq'])

    clients = clients.order_by('-date')
    client_dict = {'clients': clients}

    return render_to_response('clientlist.html', client_dict, context_instance=RequestContext(request))


def add_owner(request):
    if request.method == "POST":
        form = OwnerForm(request.POST, request.FILES)

        if form.is_valid():
            owner_name = form.cleaned_data["ownername"]
            contact = form.cleaned_data["contact"]
            print owner_name
            print contact

            try:
                newOwner = Owner.objects.create(name=owner_name, contact=contact)
                return HttpResponseRedirect(reverse_lazy('index'))
                
            except Exception as e:
                message.error(request, str(e))

    else:
        form = OwnerForm()
        return render(request, 'index.html', {'form': form})


def index(request):
    return render_to_response('index.html', {})


def delete_owner(request, pk):
    owner = get_object_or_404(Owner, pk=int(pk))
    owner.job_set.all().delete()
    owner.delete()
    return HttpResponseRedirect(reverse('index'))


def delete_job(request, pk):
    job = get_object_or_404(Job, pk=int(pk))
    job.delete()
    return HttpResponseRedirect(reverse('index'))


def set_reminder(request):

    if request.method=="POST":
        
        form = ReminderForm(request.POST)
        #print form
        success = False
        if form.is_valid():
            print form
            job_name = form.cleaned_data["job"]
            owner_name = form.cleaned_data["owner"]
            remindee = form.cleaned_data["contact"]
            
            keys = form.fields
            
            selected = keys['job']
            print selected
            print job_name
            #print form.cleaned_data
            #print form.fields

            job = Job.objects.get(name__icontains=job_name)
            owner = Owner.objects.get(name__iexact=owner_name)
            print owner.id
            print job.id

            newTrack = Tracker.objects.create(is_set=True, job_id=job.id, owner_id=owner.id, contact=remindee)
            print newTrack

            messages.add_message(request, messages.SUCCESS, "Reminder has been set")
            return HttpResponseRedirect(reverse_lazy('set_reminder'))

    else:
        form = ReminderForm()
        return render(request, 'set_reminder.html', {'form': form})


def job_form(request):
    form = forms.JobForm()
    return render(request, 'index.html', {'form': form})#sends request back, and a context dict to the view., sends instatiated form out to template


def job_form(request):

    form1 = JobForm()
    ctx = {'job_form': form1}
    return render_to_response('add_job.html', ctx, context_instance=RequestContext(request))

def rem_form(request):

    form2 = ReminderForm()
    ctx = {'rem_form': form2}
    return render_to_response('set_reminder.html', ctx, context_instance=RequestContext(request))
'''







