from .models import *

import urllib2
import urllib


def send_message(receiver, sender, text):

    request = Smslog.objects.create(
        receiver = receiver,
        message = text)

    username = "tester"
    password = "foobar"
    send_url = "http://192.168.1.50:13013/cgi-bin/sendsms"

    params = {
                'username': username,
                'password': password,
                'to'  : receiver,
                'from': sender,
                'text': text,
             }

    if True:
        full_path = send_url + '?' + urllib.urlencode(params)
        print full_path
        req = urllib2.Request(full_path)
        res = urllib2.urlopen(req)
        print "sending sms"



