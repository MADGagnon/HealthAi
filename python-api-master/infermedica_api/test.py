import infermedica_api
import requests

def parse2(symptons_str):
    myHeaders = {"app_id":"cf82ff04", "app_key":"e4ea29fdc3b01d4263da84423dc6cac0", "Content-Type": "application/json", "Accept": "application/json"}
    r = requests.post("https://api.infermedica.com/v2/parse", headers = myHeaders, data = symptons_str)
    return r

def getQuestion(sex_input, age_input, symptoms_list):

    infermedica_api.configure(app_id='cf82ff04', app_key='e4ea29fdc3b01d4263da84423dc6cac0')
    api = infermedica_api.get_api()
    symptoms = symptoms_list    #CATCH TRUE SYMPTOMS
    request = infermedica_api.Diagnosis(sex=sex_input, age=age_input)                      #CATCH

    for i in symptoms:
        json_symptoms = "{ \"text\": \""+ i + "\", \"include_tokens\": \"false\"}"
        print(json_symptoms)
        try:
            symptom_id = parse2(json_symptoms).json()["mentions"][0]["id"]
            request.add_symptom(symptom_id, 'present')
        except IndexError:
            pass

    request = api.diagnosis(request)
    rest_of_test(api, request)
    return request.question #question du resultat


def rest_of_test(api, request):
    conditionName = None
    conditionID = None
    max = 0
    while max < 0.7:

        request = api.diagnosis(request)
        print(request.question.text)  #SEND QUESTION

        for i in request.question.items:
            print(i['name'])                  #SEND QUESTION
            for j in i['choices']:
                print(j['label'])            #SEND ANSWER CHOICES
            answer = "Yes"                   #CATCH ANSWER
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

    #TODO NEW
    #TODO NEED varaible: conditionName, conditionID, max, api
    start = str(api.condition_details(str(conditionID))).find('"hint":')
    end = str(api.condition_details(str(conditionID))).find(',', start)
    print("Diagnostic: ", conditionName, "\nWith probability: ", max,"\n"+str(api.condition_details(str(conditionID)))[start+9:end-1])  # TODO SEND RESULT
    # TODO NEW /END/


getQuestion("male", 35, ["eyes hurts","my head hurts really bad", "stomac hurts", "sleepy"])

