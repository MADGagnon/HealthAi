from flask import Flask, request, redirect
import twilio.twiml
import math



app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])

def sms():
    number = request.form['From']
    message_body = request.form['Body']

    resp = twilio.twiml.Response()
    resp.message('Hello {}, you said: {}'.format(number, message_body))
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)

