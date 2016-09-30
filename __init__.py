from flask import Flask, request, redirect
import twilio.twiml

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def respond():

	body = str(request.values.get('Body', None))
	body = body.strip()
	resp = twilio.twiml.Response()
	message = ''

#	with open("/tmp/log.txt","w") as logout:
#		logout.write("something")

	if ('NOMORE' in body) or ('NOMORE' in body.upper()):
		last_time = 60
		with open("/tmp/sleep.txt","r") as fi:
			last_time = int(fi.readline())


		new_time = int(last_time/2)

		message = "Were glad that you love CatFacts! You will now receive CatFacts every %i seconds. Reply NOMORE to unsubscribe."%new_time

		with open("/tmp/sleep.txt","w") as fo:
			fo.write(str(new_time))
	else:
		message = "Invalid command, reply NOMORE to unsubscribe"

	resp.message(message)
	return str(resp)

if __name__ == "__main__":
	app.run(debug=False)