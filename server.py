from flask import Flask, request, jsonify
from flask_cors import CORS
import gspread
import random
from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import Bcrypt
from ai import *
from automator import *

from oauth2client.service_account import ServiceAccountCredentials


app = Flask(__name__)
# bcrypt = Bcrypt(app)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# app.config['SECRET_KEY'] = 'thisisasecretkey'
# db = SQLAlchemy(app)

# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = 'login'

CORS(app)


# # @login_manager.user_loader
# # def load_user(user_id):
# #     return User.query.get(int(user_id))


# # class User(db.Model, UserMixin):
# #     id = db.Column(db.Integer, primary_key=True)
# #     username = db.Column(db.String(20), nullable=False, unique=True)
# #     password = db.Column(db.String(80), nullable=False)


# class RegisterForm(FlaskForm):
#     username = StringField(validators=[
#                            InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})

#     password = PasswordField(validators=[
#                              InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})

#     confrimPassword = PasswordField(validators=[
#                              InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Confirm Password"})

#     submit = SubmitField('Register')

#     def validate_username(self, username):
#         existing_user_username = User.query.filter_by(
#             username=username.data).first()
#         if existing_user_username:
#             raise ValidationError(
#                 'That username already exists. Please choose a different one.')

#     def validate_password(self, password, confirmPassword):
#         if password != confirmPassword:
#              raise ValidationError(
#                 'That username already exists. Please choose a different one.')


# class LoginForm(FlaskForm):
#     username = StringField(validators=[
#                            InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})

#     password = PasswordField(validators=[
#                              InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})

#     submit = SubmitField('Login')




# sa = gspread.service_account(filename='script.json')
# sh = sa.open('student')

# wks = sh.worksheet("Sheet1")


scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('service_account.json', scope)
gc = gspread.authorize(creds)
# 1u3FxnKRtu5qteerQ6b3MoFVHqWaQ3lfD9u2KpYvJY5U'
# 11oC81VbhDhRqE8NY2ZNrlEXIrdsAummmLxihhPqctmw
# Open Spreadsheet by Key
sheet = gc.open_by_key('11oC81VbhDhRqE8NY2ZNrlEXIrdsAummmLxihhPqctmw')

# Select a specific sheet and pass worksheet object
wks = sheet.sheet1


@app.route("/")
def work():
    return "working"

@app.route("/fix", methods=['GET', 'POST'])
def work1():
    print("calling it")
    if request.method == 'POST':
        message = request.get_json()['message']
        msg = message['message']
        value = msg['value']
      
        if test(value)[1] == actions[0]:
            analyzeResponseParse = test(value)[0]
            formula = analyzeResponseParse[0]
            targetCell = analyzeResponseParse[1]
            insert(formula, targetCell, wks)

        elif test(value)[1] == actions[1]:
            modifyResponseParse = test(value)[0]
            print("from here", modifyResponseParse[0])
            try:
                if(modifyResponseParse[0].lower() == 'move'):
                    print("move")
                    move(modifyResponseParse[1],modifyResponseParse[2],wks)
                elif(modifyResponseParse[0].lower() == 'switch'):
                    print("switch")
                    switch(modifyResponseParse[1],modifyResponseParse[2],wks)
                else:
                    print('catch case')
                    catchPrompt = "You are an expert in google sheets and you want to help interpret what people what do do in google sheets. A user asks '{}'. Respond with the steps needed to execute the users actions and make sure they are steps that are able to be done in google sheets. Make sure the steps are clear and simple and can be understood and followed by a 5th grader".format(userInput)
                    response2 = openai.Completion.create(
                    model="text-davinci-003", 
                    prompt=catchPrompt, 
                    temperature=0, 
                    max_tokens=100
                    )
                    print(response2.choices[0].text)
            except:
                print("I could not understand your response, please try rephrasing your question")
                    

        return jsonify({'success': True, 'message':"it works"})
  
    return jsonify({'success': True, 'message':"value"})



if __name__ == "__main__":
   
    app.run(debug=True)