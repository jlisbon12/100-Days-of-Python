from twilio.rest import Client

TWILIO_SID = "ACef5d0855247b9cb19a69adbf43254c3f"
TWILIO_TOKEN = "b03a5bccd144c033d8aead6d073711e9"
TWILIO_VERF_NUM = "+14045108390"
TWILIO_VIR_NUM = "+13254408012"
class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIR_NUM,
            to=TWILIO_VERF_NUM
        )

        print(message.sid)