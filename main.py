from twilio.rest import TwilioRestClient
    # put your own credentials here
ACCOUNT_SID = 'ACfef0a61b5a52235dee7b925cb628bd8f'
AUTH_TOKEN = '38755bb8db9c8337e6e75838699e3ac0'

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

message = client.messages.create(
    to = '+16138699318', #receiver
    from_ = '+13437006039', #customer
    body = 'Hi friend, send me your symptoms separated by spaces\n',
)
print (message.sid)


#user inputs question
def get_symptoms():
    '''
    None -> None
    '''
    symptoms = input("Send me your symptoms separated by spaces\n")


print ("Hello World")
