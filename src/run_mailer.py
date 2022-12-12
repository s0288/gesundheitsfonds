from flask import Flask
from flask_mail import Mail, Message

from utils import load_okr_json, get_check_in_msg

OKR_JSON = load_okr_json()

app = Flask(__name__)
mail= Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = input("Type your email and press enter: ")
app.config['MAIL_PASSWORD'] = input("Type your password and press enter: ")
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

def send_message(recipient_email, recipient_okrs):
   msg = Message('Check-In', sender = app.config['MAIL_USERNAME'], recipients = [recipient_email])
   msg.subject = "Wie geht es dir?"
   msg.body = get_check_in_msg(recipient_okrs)
   mail.send(msg)


@app.route("/")
def index():
   for user in OKR_JSON["users"]:
      send_message(user["email"], user["okrs"])
   return "Sent"

if __name__ == '__main__':
   app.run(debug = True)
