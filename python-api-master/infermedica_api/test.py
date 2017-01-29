import infermedica_api
import requests

def parse2(symptons_str):
    myHeaders = {"app_id":"eb66ec4d", "app_key":"0dd627685ea5a3453973ea6aab7f36c1", "Content-Type": "application/json", "Accept": "application/json"}
    r = requests.post("https://api.infermedica.com/v2/parse", headers = myHeaders, data = symptons_str)
    return r

def getQuestion(sex_input, age_input, symptoms_list):
    infermedica_api.configure(app_id='eb66ec4d', app_key='0dd627685ea5a3453973ea6aab7f36c1')

    api = infermedica_api.get_api()

    symptoms = symptoms_list    #TODO CATCH TRUE SYMPTOMS
    # Create diagnosis object with initial patient information.
    # Note that time argument is optional here as well as in the add_symptom function
    request = infermedica_api.Diagnosis(sex=sex_input, age=age_input)                      #TODO CATCH

    for i in symptoms:
        json_symptoms = "{ \"text\": \""+ i + "\", \"include_tokens\": \"false\"}"
        print(json_symptoms)
        try:
            symptom_id = parse2(json_symptoms).json()["mentions"][0]["id"]
            request.add_symptom(symptom_id, 'present')
        except IndexError:
            pass

    request = api.diagnosis(request)
    return request.question #question du resultat


def rest_of_test():
    conditionID = None
    max = 0
    while max < 0.7:

        request = api.diagnosis(request)
        print(request.question.text)  #TODO SEND QUESTION

        # if request.question.type == "group_multiple":
        #     #TODO
        #     for i in request.question.items:
        #         print(i['name'])
        #         for j in i['choices']:
        #             print(j['label'])

        for i in request.question.items:
            print(i['name'])                  #TODO SEND QUESTION
            for j in i['choices']:
                print(j['label'])            #TODO SEND ANSWER CHOICES
            answer = "Yes"                   #TODO CATCH ANSWER
            if answer == "Yes":
                request.add_symptom(i["id"], 'present')
            elif answer == "No":
                request.add_symptom(i["id"], 'absent')
            elif answer == "Don't know":
                request.add_symptom(i["id"], "unknown")

    max = 0
    for i in request.conditions:
        if max < i['probability']:
            max = i['probability']
            conditionID = i["id"]


#print(request.question.items)  # list of related evidences with possible answers
# print(request.question.items[0]['id'])
# print(request.question.items[0]['name'])
# print(request.question.items[0]['choices'])  # list of possible answers
# print(request.question.items[0]['choices'][0]['id'])  # answer id
# print(request.question.items[0]['choices'][0]['label'])  # answer label
#
# Access list of conditions with probabilities
#print(request.conditions)
#print(request.conditions[0]['id'])

#print(max)
#print(conditionID)
for i in request.conditions:
    print(i['name'])
    print(i['probability'])

#print(api.explain(request, target_id='c_62'))

# # Next update the request and get next question:
# # Just example, the id and answer shall be taken from the real user answer
# request.add_symptom(request.question.items[0]['id'], request.question.items[0]['choices'][1]['id'])
#
# # call diagnosis method again
# request = api.diagnosis(request)
#
# # ... and so on, until you decide to stop the diagnostic interview.
#
getQuestion("male", 35, ["eyes hurts","my head hurts really bad", "stomac hurts", "sleepy"])
