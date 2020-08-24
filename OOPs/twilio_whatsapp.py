import os
from twilio.rest import  Client

whatsapp_client=Client()

from_twilio_number='whatsapp:+14155238886'
to_whatsapp_number='whatsapp:+19802663220'


whatsapp_client.messages.create(body='This is test it from shaishav',
            from_=from_twilio_number,to=to_whatsapp_number)