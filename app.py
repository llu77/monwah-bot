
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import os

app = Flask(__name__)

@app.route("/whatsapp", methods=['POST'])
def whatsapp_reply():
    incoming_msg = request.form['Body']
    reply_text = f"منوه: تلقيت رسالتك - '{incoming_msg}'، لكن الرد الصوتي غير مفعل حالياً."
    resp = MessagingResponse()
    msg = resp.message(reply_text)
    return str(resp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
