import openai
import gspread
import re
import os
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv('openai.api_key')

# modifyPrompt = "You are an expert in google sheets and you want to help interpret what people what do do in google sheets. A user asks '{}'. The user can only move data, wrap the text in the cell or column, or switch data.Check if user wants to move, wrap or switch. If the user wants to move data, only respond with: move, [old cell], [new cell]. If the user wants to wrap the text in a cell or column, only respond with: fit, [target column]. If the user wants to switch data, only respond with: switch, [first cell], [second cell].'".format(userInput) 


actions = ['analyze', 'modify']

def test(userInput):
    userPrompt = "You are an expert in google sheets and you want to help interpret what people what do do in google sheets. A user asks '{}'. Is the users problem able to be solved with a google sheets formula? Or do they want to modify the sheet? Respond with one word, modify or formula".format(userInput)

    response = openai.Completion.create(
        model="text-davinci-003", 
        prompt=userPrompt, 
        temperature=0, 
        max_tokens=25
        )

    botResponse = response.choices[0].text

    if "formula" in botResponse.lower():
        analyzePrompt = "You are an expert in google sheets and you want to help interpret what people what do do in google sheets. A user asks '{}'. If the user did not specify a target cell, put 'none' in the target cell section. Respond with the formula, using colon format the user wants as well as the target cell the user want to put the formula in in the format: [formula], [target cell]".format(userInput)
        response2 = openai.Completion.create(
        model="text-davinci-003", 
        prompt=analyzePrompt, 
        temperature=0, 
        max_tokens=25
        )
        # print(response2)
        analyzeResponse = response2.choices[0].text.strip().replace(" ", "")

        analyzeResponseParse = analyzeResponse.split(',')
        return [analyzeResponseParse, actions[0]]

    else:
        modifyPrompt = "You are an expert in google sheets and you want to help interpret what people want to do in google sheets. A user asks '{}'. The user can only move data or switch data. For all answers, do not add 'Answer:' to the beginning. If the user wants to move data, only respond with: 'move, [old cell], [new cell]'.  If the user wants to switch data, only respond with: 'switch, [first cell], [second cell]'.".format(userInput)
        response2 = openai.Completion.create(
        model="text-davinci-003", 
        prompt=modifyPrompt, 
        temperature=0, 
        max_tokens=25
        )
        # print(response2)
        modifyResponse = response2.choices[0].text.strip().replace(" ", "")
        modifyResponseParse = modifyResponse.split(',')
        # print(modifyResponseParse)
        return [modifyResponseParse, actions[1]]
       
  