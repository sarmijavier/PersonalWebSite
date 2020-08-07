from flask import Flask, render_template, flash, redirect, request, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import EmailField
import pyrebase
import os

app = Flask(__name__, template_folder='templates', static_folder='static')
bootstrap = Bootstrap(app)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY']= SECRET_KEY

firebaseConfig = {
  "apiKey": "AIzaSyDwM0tnkHrJNwWU6ETFSQVzE9h4lrRqNxw",
  "authDomain": "messageswebsite-4130e.firebaseapp.com",
  "databaseURL": "https://messageswebsite-4130e.firebaseio.com",
  "projectId": "messageswebsite-4130e",
  "storageBucket": "messageswebsite-4130e.appspot.com",
  "messagingSenderId": "572331620753",
  "appId": "1:572331620753:web:addd03690fda0d335ec230"
}

firebase = pyrebase.initialize_app(firebaseConfig)

class ContactForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired()])
    message = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Send')


@app.errorhandler(500)
def server_error(error):
    return render_template('505.html', error=error)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)


@app.route('/')
def whoami():
    contact_form = ContactForm()

    return render_template('whoami.html', contact_form=contact_form)


@app.route('/portfolio')
def portfolio():

    contact_form = ContactForm()

    return render_template('portfolio.html', contact_form=contact_form)

@app.route('/blog')
def blog():
    contact_form = ContactForm()

    return render_template('blog.html', contact_form=contact_form)

@app.route('/neverStopLearning')
def never():
    return render_template('neverStopLearning.html')


@app.route('/bogota')
def bogota():
    return render_template('bogota.html')


@app.route('/contact', methods=['GET','POST'])
def contact():

    contact_form = ContactForm()

    if contact_form.validate_on_submit():
        email = contact_form.email.data
        message =  contact_form.message.data
        flash('Thank you, I\'ll contact you soon')
        data = {
            'email': email,
            'message': message
        }
        db = firebase.database()
        db.child('messages').push(data)
        return redirect(url_for('whoami'))


if __name__ == "__main__":
    app.run(debug=1)