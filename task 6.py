from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)
mail = Mail(app)

app.config['MAIL_SERVER']='smtp@gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'pkpremk77@gmail.com'
app.config['MAIL_PASSWORD'] = 'Mypasswordis'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route("/")
def index():
    msg = Message('Hello', sender='pkpremk77@gmail.com', recipients=['sindhukannan211@gmail.com'])
    msg.body = "Hello sindhu this msg is from pk"
    mail.send(msg)
    return "Message Sent"


if __name__ == '__main__':
    app.run(debug=True)