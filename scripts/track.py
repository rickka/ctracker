
from smsremind.models import *
from smsremind.utils import send_message
from django.utils.timezone import utc
from datetime import datetime


def check_for_reminder():
    trackset = Reminder.objects.filter(is_set=True)
    if trackset:
        for track in trackerset:
            if track.count >= 3:
                #unset the reminder since its gone 3 times
		track.is_set = False
                pass

	    else:
                current_time = datetime.utcnow().replace(tzinfo=utc)
                time_left = track.contract.expiry.days - current_time

                # if time left is less than 90 days, start sending reminder weekly and 
                if time_left.days < 90:

                    text = 'CONTRACT RENEWAL PENDING: %s, expires in %s days, on %s' % (track.contract.title, time_left, track.expiry.strftime('%B/%d'))
                    sender = '8008'

                    #send_message(track.contact.dcontact, sender, text)
		    logger = SmsLog.objects.create(text=text, receiver=track.contract.dcontact)
                    logger.save()
		    print 'sending messages'
                
                    track.count += 1
                    track.save()
'''          
    #queryset to send reminders to
    to_send = Tracker.objects.filter(is_active=True)
    if to_send:
        for track in trackerset:
            dead_line = track.job.deadline
            job = track.job.name
            owner = str(track.owner.name)
'''            
            
def run():
    check_for_reminder()
        
