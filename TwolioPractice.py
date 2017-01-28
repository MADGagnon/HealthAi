from twilio.rest import TwilioRestClient
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

# textToCellphone('+15142967873') ex of function use


