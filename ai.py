import openai
import gspread
import re


# Open Spreadsheet by Key

# Load your API key from an environment variable or secret management service
openai.api_key = "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"


# userInput = "get the standard deviation of B11-B13"

# # userPrompt = "You are an exert in google sheets and you want to help interpret what people what do do in google sheets. A user asks 'I want insert the value 52 into cell b3'. Is the user trying to insert data, delete data, average data, sum data, or graph data? Respond with an array that has the function in one word, the range of cells the user wants to interact with (if the user is just targeting one cell just put one cell), the target cell, and the value that the user wants to have in the target cell."
# userPrompt = "You are an expert in google sheets and you want to help interpret what people what do do in google sheets. A user asks '{}'. Is the user trying to move around the data in sheet or trying to analyze the data in the sheet? Respond with one word, modify or analyze".format(userInput)

# response = openai.Completion.create(
#     model="text-davinci-003", 
#     prompt=userPrompt, 
#     temperature=0, 
#     max_tokens=25
#     )

# botResponse = response.choices[0].text
# # print(botResponse)

# if "analyze" in botResponse.lower():
#     analyzePrompt = "You are an expert in google sheets and you want to help interpret what people what do do in google sheets. A user asks '{}'. If the user did not specify a target cell, put 'none' in the target cell section. Respond with the formula, using colon format the user wants as well as the target cell the user want to put the formula in in the format: [formula], [target cell]".format(userInput)
#     response2 = openai.Completion.create(
#     model="text-davinci-003", 
#     prompt=analyzePrompt, 
#     temperature=0, 
#     max_tokens=25
#     )

#     analyzeResponse = response2.choices[0].text.strip().replace(" ", "")
#     # print(analyzeResponse)
#     analyzeResponseParse = analyzeResponse.split(',')
#     # print(analyzeResponseParse)

#     # worksheet.update(analyzeResponseParse[1], analyzeResponseParse[0], value_input_option='USER_ENTERED')
# else:
#     # print('you want to modify!')
#     pass

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