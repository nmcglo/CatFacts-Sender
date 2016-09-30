import sys
import os
from time import sleep
from catfactgen import catfactgenerator
from twilio.rest import TwilioRestClient


#ACCOUNT_SID = os.environ['TWILIOSID']
#AUTH_TOKEN = os.environ['TWILIOTOKEN']

ACCOUNT_SID = 'AG28106028FJcdg335j8j099fjghaieiw2' #Not real SID - change to your own
AUTH_TOKEN = 'f28gjalkdjaaadwigovbbnjwee8259fd' #Not real token - change to your own

class CatSender(object):
    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

    toNum = "+15551002222"
    fromNum = "+15551003333"

    def send(self,txtbody):
        self.client.messages.create(
        to = self.toNum,
        from_ = self.fromNum,
        body = txtbody
        )

    def welcome(self):
        response = "Thank you for subscribing to CatFacts! "
        response += "The #1 service for the interesting and useful facts about our feline friends every 10 minutes! "
        response += "Text NOMORE to unsubscribe. Std.Msg rates apply"
        self.send(response)

    def run(self):
        with open("/tmp/sleep.txt","w") as fo: #places 
            fo.write("600")
        print("Starting CatFact Sender")
        catgen = catfactgenerator()
        print("Generator Started")
        self.welcome()
        print("Welcome Sent!")

        sleep(30)
        while(True):
            catfact = catgen.getfact()
            self.send(catfact)
            print("CatFact Sent!")

            sleepTimeFile = open('/tmp/sleep.txt','r')
            s = sleepTimeFile.readline().strip()
            sleepTimeFile.close()
            sleepTime = int(s)
            print("Sleep Time: %i seconds"%sleepTime)

            sleep(sleepTime)


if __name__ == '__main__':
    catsender = CatSender()
    catsender.run()