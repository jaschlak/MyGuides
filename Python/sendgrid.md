
# Sendgrid

    Simple example from sendgrid on how to send a sendgrid e-mail.
    
    
### Prerequisite

    sendgrid account
    sendgrid api key
    
    Python 3.6 or greater
    import sendgrid
    
## Sample Code
# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
import sendgrid
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='from@example.com',
    to_emails='to@example.com',
    subject='Sending with Twilio SendGrid is Fun',
    html_content='<strong>and easy to do anywhere, even with Python</strong>')
try:
    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e)
    
    
## Supreme example found on github:

    https://github.com/sendgrid/sendgrid-python/blob/main/examples/helpers/mail_example.py
    
## Sample Code (template variables):


Sendgrid example including template variables:

    
    #!/usr/bin/env python3
    import os
    from sendgrid.helpers.mail import Mail
    from sendgrid import SendGridAPIClient

    # from address we pass to our Mail object, edit with your name
    FROM_EMAIL = '<from@example.com>'

    # update to your dynamic template id from the UI
    TEMPLATE_ID = 'd-<sendgrid_template_id>'                                # links e-mail to template made in sendgrid dynamic templates (subject, place, event)

    # list of emails and preheader names, update with yours
    TO_EMAILS = [('<to@example.com>', '<to_name>')
                 # add more e-mails if you want,
                 # ('<your_email+1@domain.com>', '<to_name>')
                 ]


    def SendDynamic():
        """ Send a dynamic email to a list of email addresses

        :returns API response code
        :raises Exception e: raises an exception """
        # create Mail object and populate
        message = Mail(
            from_email=FROM_EMAIL,
            to_emails=TO_EMAILS)
        # pass custom values for our HTML placeholders
        message.dynamic_template_data = {
            'subject': 'SendGrid Development',                              # sendgrid example variables and values
            'place': 'New York City',
            'event': 'Twilio Signal'
        }
        message.template_id = TEMPLATE_ID
        # create our sendgrid client object, pass it our key, then send and return our response objects
        try:
            sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))      # sendgrid api saved as environmental variable    
            response = sg.send(message)
            code, body, headers = response.status_code, response.body, response.headers
            print("Response Code: {0} ".format(code))
            print("Response Body: {0} ".format(body))
            print("Response Headers: {0} ".format(headers))
            print("Message Sent!")
            return str(response.status_code)
        except Exception as e:
            print("Error: {0}".format(e))


    if __name__ == "__main__":
        SendDynamic()
