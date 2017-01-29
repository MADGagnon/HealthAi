from flask import Flask, request, session
import twilio.twiml
from twilio.rest import TwilioRestClient
import infermedica_api
from twilio import twiml
import main
import sys
sys.path.insert(0, '/python-api-master/infermedica_api')

import test


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



# The session object makes use of a secret key.
SECRET_KEY = 'a secret key'
app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/', methods=['GET', 'POST'])

def sms():

    number = request.form['From']
    message_body = request.form['Body']


    """Respond with the number of text messages sent between two parties."""
    # Increment the counter
    counter = session.get('counter', 0)
    name1 = session.get('name1', '')
    age1 = session.get('age1', '')
    sexe1 = session.get('sexe1', '')
    user_info1 = session.get('user_info1', '')
    counter += 1

    # Save the new counter value in the session
    session['counter'] = counter

    from_number = request.values.get('From')

    if message_body == "reset" or counter == 1:
        counter = 1
        session['counter'] = counter
        resp = twiml.Response()
        resp.message("Hi there, I'm [SickVick]! Let's get started.\n\n"+main.user_name())

    elif counter == 2 :

        session['name1'] = request.form['Body']
        resp = twiml.Response()
        resp.message(main.age())

    elif counter == 3 :

        session['age1'] = request.form['Body']
        resp = twiml.Response()
        resp.message(main.sexe())

    elif counter == 4 :

        session['sexe1'] = request.form['Body']
        resp = twiml.Response()
        session['user_info1'] = [name1, age1, sexe1]
        resp.message("Please send me your symptoms separated by commas.\n")

    else :
        name = request.form['Body']
        resp = twiml.Response()
        resp.message("name")
    # Put it in a TwiML response






    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
