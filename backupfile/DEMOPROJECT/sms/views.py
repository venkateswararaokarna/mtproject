from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render,redirect
import datetime

from .models import ReceivedMessages

from twilio.twiml.messaging_response import MessagingResponse


from flask import Flask , request
from twilio import twiml


#number = request.form['From']

#print(number)

@csrf_exempt

def sms_response(request):

    # Start our TwiML response
    print("req is ----",request)

    from_number = request.POST.get('From', '')
    body = request.POST.get('Body', '')
    print(body)
    print(from_number)


    resp = MessagingResponse()


    # Add a text message
    date = datetime.datetime.now()
    if(from_number):
        ReceivedMessages.objects.create(phonenumber = from_number,body = body,received_date = date)

        count = ReceivedMessages.objects.count()

        msg = resp.message(f"your num is : {from_number} andyou said {body} \n have a nice day \n count is {count}")
    else:
        msg = resp.message("Nothing received")
        return redirect('homepage')



    # Add a picture message

    #msg.media("https://demo.twilio.com/owl.png")



    return HttpResponse(str(resp))
