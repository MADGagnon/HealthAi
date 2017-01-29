from flask import Flask, request, session
import twilio.twiml
from twilio.rest import TwilioRestClient
import infermedica_api

def testing():
    infermedica_api.configure(app_id='eb66ec4d', app_key='0dd627685ea5a3453973ea6aab7f36c1')

    api = infermedica_api.get_api()
    symtoms = ["heart", "headache", "craving"]
    # Create diagnosis object with initial patient information.
    # Note that time argument is optional here as well as in the add_symptom function
    request = infermedica_api.Diagnosis(sex='male', age=35)

    for i in symtoms:
        symptom_id = api.search(i)[0]["id"]
        print(symptom_id)
        request.add_symptom(symptom_id, 'present')
    #
    # request.add_symptom('s_21', 'present')
    # request.add_symptom('s_98', 'present')
    # request.add_symptom('s_107', 'absent')

    # request.set_pursued_conditions(['c_33', 'c_49'])  # Optional

    # call diagnosis
    request = api.diagnosis(request)

    # # Access question asked by API
    # print(request.question)
    # print(request.question.text)  # actual text of the question
    # print(request.question.items)  # list of related evidences with possible answers
    # print(request.question.items[0]['id'])
    # print(request.question.items[0]['name'])
    # print(request.question.items[0]['choices'])  # list of possible answers
    # print(request.question.items[0]['choices'][0]['id'])  # answer id
    # print(request.question.items[0]['choices'][0]['label'])  # answer label

    # Access list of conditions with probabilities
    # print(request.conditions)
    # print(request.conditions[0]['id'])
    print(request.conditions[0]['name'])
    # print(request.conditions[0]['probability'])

    # Next update the request and get next question:
    # Just example, the id and answer shall be taken from the real user answer
    request.add_symptom(request.question.items[0]['id'], request.question.items[0]['choices'][1]['id'])

    # call diagnosis method again
    request = api.diagnosis(request)

    # ... and so on, until you decide to stop the diagnostic interview.
    return request.conditions[0]['name']

def textToCellphone(phoneNbr):
    # put your own credentials here
    ACCOUNT_SID = 'ACbcdd2baea53b4be6b8732978947cf41b'
    AUTH_TOKEN = '9c7ed39432e7db891055ea09f17aaa1d'

    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

    client.messages.create(
        to=phoneNbr,
        from_='+14387951624',
        body='hey from McHacks2017',
    )


app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])

def sms():

    # Increment the counter
    counter = session.get('counter', 0)
    counter += 1

    # Save the new counter value in the session
    session['counter'] = counter

    number = request.form['From']
    message_body = request.form['Body']

    resp = twilio.twiml.Response()
    # resp.message('Hello {}, you said: {}'.format(number, message_body))
    resp.message(counter)
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
