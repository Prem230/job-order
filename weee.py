from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Mypasswordis@23@ localhost:5432/Sunday'
db = SQLAlchemy(app)



class students(db.Model):

   __tablename__ = 'Sunday'
   id = db.Column('student_id', db.Integer, primary_key = True)
   name = db.Column(db.String(100))
   city = db.Column(db.String(50))
   addr = db.Column(db.String(200))
   pin = db.Column(db.String(10))



if __name__ =='__main__':
   app.run(debug=True)