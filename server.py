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
# from ai import *
from automator import *


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




sa = gspread.service_account(filename='script.json')
sh = sa.open('student')

wks = sh.worksheet("Sheet1")


@app.route("/")
def work():
    return "working"

@app.route("/fix", methods=['GET', 'POST'])
def work1():
    print("calling it")
    if request.method == 'POST':
    # #     pass
    # #     try:
        message = request.get_json()['message']
    # #         # do something with the message here...
        msg = message['message']
        value = msg['value']
        # analyzeResponseParse = test(value)
        # formula = analyzeResponseParse[0]
        # targetCell = analyzeResponseParse[1]
        # insert(formula, targetCell, wks)
    #     print("here", value)
        return jsonify({'success': True, 'message':"formula"})
    #     except (TypeError, KeyError):
    #         # handle the case where the request payload is invalid or missing the "message" field
    #         return jsonify({'success': False, 'message': 'Invalid or missing request payload'})
    # else:
    #     # handle the case where the HTTP method is not POST
    return jsonify({'success': True, 'message':"value"})

# def work1():
#     # if request.method == "OPTIONS":
#     message = request.get_json()['message']
#     msg = message['message']
#     value = msg['value']
#     analyzeResponseParse = test(value)
#     formula = analyzeResponseParse[0]
#         # pass
#         # if message:
#         #     return "message received from api"
#         # else:
#         #     return "wtf api"
#     # else:
#     # return request.method 
#     # message = {'text': 'goodbye from Flask!'}
#     # analyzeResponseParse = test(value)
#     # formula = analyzeResponseParse[0]
#     # targetCell = analyzeResponseParse[1]
#     # insert(formula, targetCell, wks)
#     # # wks.update(test(value)[1], test(value)[0], value_input_option='USER_ENTERED')
#     # response = {'status': 'ok'}
#     return "jsonify(message)"



# @app.route('/api/messages', methods=['POST', 'GET'])
# def messages():

#     message = request.get_json()['message']
#     print(message)
#     msg = message['message']
#     value = msg['value']
#     print(value)
#     print(test(value))
#     analyzeResponseParse = test(value)
#     formula = analyzeResponseParse[0]
#     targetCell = analyzeResponseParse[1]
#     insert(formula, targetCell, wks)
#     wks.update(test(value)[1], test(value)[0], value_input_option='USER_ENTERED')
#     response = {'status': 'ok'}

#     return jsonify(response)



if __name__ == "__main__":
   
    app.run(debug=True)