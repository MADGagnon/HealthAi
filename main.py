from twilio.rest import TwilioRestClient

def user_name():
    name = str(input("What's your name?\n"))
    return name

def set_up():
    #if receive text from user (through HTTP)
    print("Hi there, I'm [SickVick]")

    agreeToSignUp = str(input("Would you like to sign up for [SickVick]? [Yes or No]\n"))

    if agreeToSignUp.lower() == "no":
        print("Ok, pce.")
        return None
    else:
        print("Awesome! Let's set you up!\n")

        name = user_name()
        sexe = str(input("What's your biological sexe?\n"))
        age = str(input("What's your age?\n"))
        
        userInfo = [name, sexe, age]
        return userInfo
            

def user_symptoms():
    symptoms = str(input("Please send me your symptoms.\n"))
    return symptoms

def textToCellphone(phoneNbr):
    ACCOUNT_SID = 'ACfef0a61b5a52235dee7b925cb628bd8f'
    AUTH_TOKEN = '38755bb8db9c8337e6e75838699e3ac0'

    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

    message = client.messages.create(
        to = phoneNbr,
        from_ = '+13437006039', 
        body = 'Hi' + name,
    )

#main
name = ''
set_up()
textToCellphone('+16138699318')
#user_symptoms()



    
    
