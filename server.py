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

CORS(app)

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('service_account.json', scope)
gc = gspread.authorize(creds)
# 1u3FxnKRtu5qteerQ6b3MoFVHqWaQ3lfD9u2KpYvJY5U'
# 11oC81VbhDhRqE8NY2ZNrlEXIrdsAummmLxihhPqctmw

# Open Spreadsheet by Key

global sheetKey
global sheet
global wks
sheetKey = '11oC81VbhDhRqE8NY2ZNrlEXIrdsAummmLxihhPqctmw'
# sheetKey = '1E7wsTz5dAgxCFgldGjfAMKpbhR4pBDjKCVhkWrZYESk'

@app.route("/", methods=['POST'])
def work2():
    if request.method == 'POST':
        global sheetKey
        global wks
        global sheet
        newKey = request.get_json()['key']
        print(newKey)
        sheet = gc.open_by_key(newKey)
        wks = sheet.sheet1
        sheet = newKey
        print("Setting key ")
        return jsonify({'content': "we changed the key"})



sheet = gc.open_by_key(sheetKey)

# Select a specific sheet and pass worksheet object
wks = sheet.sheet1




@app.route("/fix", methods=['GET', 'POST'])
def work1():
    print("calling it")
    if request.method == 'POST':
        message = request.get_json()['message']
        value = message['message']
        value = value['value']
        if test(value)[1] == actions[0]:
            analyzeResponseParse = test(value)[0]
            formula = analyzeResponseParse[0]
            targetCell = analyzeResponseParse[1]
            insert(formula, targetCell, wks)

        elif test(value)[1] == actions[1]:
            modifyResponseParse = test(value)[0]
            # print("from here", modifyResponseParse[0])
            try:
                if(modifyResponseParse[0].lower() == 'move'):
                    # print("move")
                    move(modifyResponseParse[1],modifyResponseParse[2],wks)
                elif(modifyResponseParse[0].lower() == 'switch'):
                    # print("switch")
                    switch(modifyResponseParse[1],modifyResponseParse[2],wks)
                else:
                    # print("edge case")
                    catchPrompt ="You are an expert in google sheets and you want to help interpret what people what do do in google sheets. A user asks '{}'. Respond with the steps needed to execute the users actions and make sure they are steps that are able to be done in google sheets. Make sure the steps are clear and simple and can be understood and followed by a 5th grader".format(modifyResponseParse)
                    responseTest = openai.Completion.create(
                    model="text-davinci-003", 
                    prompt=catchPrompt, 
                    temperature=0, 
                    max_tokens=100
                    )
                    instruction = responseTest.choices[0].text
                    print(instruction)
                    return jsonify({'success': True, 'message':instruction})
            except:
                print("I could not understand your response, please try rephrasing your question")
                    

        return jsonify({'success': True, 'message':"I have finished the task"})
  
    return jsonify({'success': True, 'message':"value"})



if __name__ == "__main__":
   
    app.run(debug=True)