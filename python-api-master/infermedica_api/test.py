import infermedica_api
import requests

def parse2(symptons_str):
    myHeaders = {"app_id":"eb66ec4d", "app_key":"0dd627685ea5a3453973ea6aab7f36c1", "Content-Type": "application/json", "Accept": "application/json"}
    r = requests.post("https://api.infermedica.com/v2/parse", headers = myHeaders, data = symptons_str)
    return r

infermedica_api.configure(app_id='eb66ec4d', app_key='0dd627685ea5a3453973ea6aab7f36c1')

api = infermedica_api.get_api()

symtoms = ["heart","my head hurts really bad", "headache", "heart"]
# Create diagnosis object with initial patient information.
# Note that time argument is optional here as well as in the add_symptom function
request = infermedica_api.Diagnosis(sex='male', age=35)

for i in symtoms:
    json_symptoms = "{ \"text\": \""+ i + "\", \"include_tokens\": \"false\"}"
    print(json_symptoms)
    try:
        symptom_id = parse2(json_symptoms).json()["mentions"][0]["id"]
        request.add_symptom(symptom_id, 'present')
    except IndexError:
        pass
    #print(symptom_id)




# request.add_symptom('s_21', 'present')
# request.add_symptom('s_98', 'present')
# request.add_symptom('s_107', 'absent')

#request.set_pursued_conditions(['c_33', 'c_49'])  # Optional

# call diagnosis
request = api.diagnosis(request)

# Access question asked by API
print(request.question)
#

#TODO send question
print(request.question.text)  # actual text of the question

if request.question.type == "group_multiple":
    #TODO
    pass


#print(request.question.items)  # list of related evidences with possible answers
# print(request.question.items[0]['id'])
# print(request.question.items[0]['name'])
# print(request.question.items[0]['choices'])  # list of possible answers
# print(request.question.items[0]['choices'][0]['id'])  # answer id
# print(request.question.items[0]['choices'][0]['label'])  # answer label
#
# # Access list of conditions with probabilities
# #print(request.conditions)
# #print(request.conditions[0]['id'])
# print(request.conditions[0]['name'])
# #print(request.conditions[0]['probability'])
#
# # Next update the request and get next question:
# # Just example, the id and answer shall be taken from the real user answer
# request.add_symptom(request.question.items[0]['id'], request.question.items[0]['choices'][1]['id'])
#
# # call diagnosis method again
# request = api.diagnosis(request)
#
# # ... and so on, until you decide to stop the diagnostic interview.
#
