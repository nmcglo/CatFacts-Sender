from flask import Flask, request, redirect
import twilio.twiml

app = Flask(__name__)

callers = {
    "+15551112222": "Adelle",
    "+15551113333": "Betty",
    "+15551114444": "Caroline",
}

@app.route("/", methods=['GET', 'POST'])
def hello_texter():
    """Respond and greet the texter by name."""

    from_number = request.values.get('From', None)
    if from_number in callers:
        message = callers[from_number] + ", thanks for the message!"
    else:
        message = "I don't know you but, thanks for the message!"

    resp = twilio.twiml.Response()
    resp.message(message)

    return str(resp)

if __name__ == "__main__":
    app.run(debug=False)