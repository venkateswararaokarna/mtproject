from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
from .models import Messages
from sms.models import ReceivedMessages
from datetime import datetime, timezone

def hi(request):
    return render(request,'DEMOAPP/hi.html')

def hi(request):
    if(request.POST.get('phone')):

        try:
            phone = request.POST['phone']
            body = request.POST['body']
        except:
            return render(request, 'DEMOAPP/hi.html')
        print('phoneeeeeee-------',phone)
        print('body-------',body)
        from twilio.rest import Client

        # Your Account SID from twilio.com/console
        account_sid = "AC372abf3a0b656698a954db55136d74c7"
        # Your Auth Token from twilio.com/console
        auth_token = "c15d663e88d887cce85aee0e90f21c3d"

        client = Client(account_sid, auth_token)
        #date = datetime.datetime.now()
        date = datetime.now(timezone.utc)
        try:

            message = client.messages.create(
                to=f"+91{phone}",
                from_="+16146605534",
                body=body)

            print(message.sid)

            Messages.objects.create(phonenumber = phone,body = body,sent_date = date)
            count = Messages.objects.count()



        except Exception as e:
            return render(request,'DEMOAPP/hi.html',{'failedmsg':'Message sent Failed'})

        return render(request,'DEMOAPP/hi.html',{'phone':phone,'sid':message.sid,'count' : count,'msg':'Message sent'})
    return render(request,'DEMOAPP/hi.html')


def webhooks(request):
    data = ReceivedMessages.objects.all()
    
    return render(request,"DEMOAPP/webhooks.html",{'data':data})

def sentmessages(request):

    data = Messages.objects.all()

    return render(request,"DEMOAPP/sentmessages.html",{'data':data})

from flask import Flask , request
from twilio import twiml

app = Flask(__name__)



@app.route('/sms', methods=['POST'])
def sms():


    number = request.form['From']

    message_body = request.form['Body']

                

    resp = twiml.Response()

    resp.message('Hello your number is : {}, you said: {}'.format(number, message_body)) 

    return str(resp)

                            

if __name__ == '__main__':
    

    app.run()

