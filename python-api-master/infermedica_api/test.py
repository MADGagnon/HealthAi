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


def rest_of_test(api):
    conditionName = None
    conditionID = None
    max = 0
    while max < 0.7:

        request = api.diagnosis(request)
        print(request.question.text)  #TODO SEND QUESTION

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

        for i in request.conditions:
            if max < i['probability']:
                max = i['probability']
                conditionID = i["id"]
                conditionName = i["name"]


#TODO BESOINS VARIABLE max, conditionName, conditionID defini dans rest_of_test
print("Diagnostic: ", conditionName, "\n With probability: ", max)    #TODO SEND RESULT


# DOESNT WORK
# #TODO IF WANT TO KNOW WHY IT SELECTIONNED THIS CONDITION SEND THIS
# for i in api.explain(request, target_id= conditionID)["supporting_evidence"]:
#     print(i["name"])        #TODO SEND supporting evidence that you have this evidence
#DOESNT WORK


getQuestion("male", 35, ["eyes hurts","my head hurts really bad", "stomac hurts", "sleepy"])
