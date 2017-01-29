from twilio.rest import TwilioRestClient

#def receiveText():

def textToCellphone(phoneNbr):
    ACCOUNT_SID = 'ACfef0a61b5a52235dee7b925cb628bd8f'
    AUTH_TOKEN = '38755bb8db9c8337e6e75838699e3ac0'

    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

    message = client.messages.create(
        to = phoneNbr,
        from_ = '+13437006039', 
        body = 'Hi ',
    )

def user_name():
    name = str(input("What's your name?\n"))
    return name

def set_up():
    #if receive text from user (through HTTP)
    print("Hi there, I'm [SickVick]! Let's get started.\n")

    name = user_name()
    sexe = str(input("What's your biological sexe?\n"))
    age = str(input("What's your age?\n"))
    
    userInfo = [name, sexe, age]
    return userInfo
            

def user_symptoms():
    symptoms = str(input("Please send me your symptoms separated by commas.\n"))
    symptoms = [str(i) for i in symptoms.split(",")]
    return symptoms


#main
#receiveText()
textToCellphone('+16138699318')
set_up()
user_symptoms()



    
    
