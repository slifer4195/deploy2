import openai
import gspread
import re
import os
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv('openai.api_key')



def test(userInput):
    userPrompt = "You are an expert in google sheets and you want to help interpret what people what do do in google sheets. A user asks '{}'. Is the user trying to move around the data in sheet or trying to analyze the data in the sheet? Respond with one word, modify or analyze".format(userInput)
    response = openai.Completion.create(
    model="text-davinci-003", 
    prompt=userPrompt, 
    temperature=0, 
    max_tokens=25
    )
    botResponse = response.choices[0].text

    if "analyze" in botResponse.lower():
        analyzePrompt = "You are an expert in google sheets and you want to help interpret what people what do do in google sheets. A user asks '{}'. If the user did not specify a target cell, put 'none' in the target cell section. Respond with the formula, using colon format the user wants as well as the target cell the user want to put the formula in in the format: [formula], [target cell]".format(userInput)
        response2 = openai.Completion.create(
        model="text-davinci-003", 
        prompt=analyzePrompt, 
        temperature=0, 
        max_tokens=25
        )

        analyzeResponse = response2.choices[0].text.strip().replace(" ", "")
        # print(analyzeResponse)
        analyzeResponseParse = analyzeResponse.split(',')
    # print(analyzeResponseParse)

    # worksheet.update(analyzeResponseParse[1], analyzeResponseParse[0], value_input_option='USER_ENTERED')
    else:
        # print('you want to modify!')
        pass
    return analyzeResponseParse