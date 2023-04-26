# from automator import *

# from oauth2client.service_account import ServiceAccountCredentials
# scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
# creds = ServiceAccountCredentials.from_json_keyfile_name('service_account.json', scope)
# gc = gspread.authorize(creds)
# # 1u3FxnKRtu5qteerQ6b3MoFVHqWaQ3lfD9u2KpYvJY5U'
# # 11oC81VbhDhRqE8NY2ZNrlEXIrdsAummmLxihhPqctmw

# # Open Spreadsheet by Key

# global sheetKey
# global sheet
# global wks
# sheetKey = '1pwhxdqlBGVYWHSLPwaOLgbJfPqFANMEa8uoqZFpmL-A'
# sheet = gc.open_by_key(sheetKey)

# # Select a specific sheet and pass worksheet object
# wks = sheet.sheet1



# def test_col_to_num():
#     assert col_to_num('A') == 1  #regular case
#     assert col_to_num('AA') == 27 #edge
#     assert col_to_num('?') == -1 #error case


# def test_num_to_col():
#     assert num_to_col(1) == 'A'
#     assert num_to_col(27) == 'AA'
#     assert num_to_col(-1) == ''


# def test_delete():
#     # Create a mock worksheet object
#     delete('A1', wks)
#     value = wks.cell(1, 1).value
#     assert value == None

#     delete('z26', wks)
#     value = wks.cell(26, 26).value
#     assert value == None

#     delete('zz', wks)
#     value = wks.cell(26, 26).value
#     assert value == None


# # Functionality: Move and maintain current value/formula into new cell. This means, if formula says =A3+B3, it should stay =A3+B3 when moved
# def test_move():
#     # grab formula or value
#     move('A1','B1', wks)
#     value1 = wks.cell(1, 1).value
#     value2 = wks.cell(2, 1).value
#     assert value1 == value2

#     move('Z26','A1', wks)
#     value1 = wks.cell(26, 26).value
#     value2 = wks.cell(1, 1).value
#     assert value1 == value2

#     move('A1','A1', wks)
#     value1 = wks.cell(1, 1).value
#     value2 = wks.cell(1, 1).value
#     assert value1 == value2

# # test_delete()

# def test_switch():
#     switch('A1', 'B1', wks)
#     temp1 = wks.cell(1, 1).value
#     temp2 = wks.cell(1, 2).value
#     assert temp1 == temp2

#     switch('A1', 'A26', wks)
#     temp1 = wks.cell(1, 1).value
#     temp2 = wks.cell(26, 1).value
#     assert temp1 == temp2


#     switch('A1', 'A1', wks)
#     temp1 = wks.cell(1, 1).value

#     assert temp1 == temp2

# def test_insert():
#     wks.cell(1, 1).value = 2
#     wks.cell(2, 1).value = 2
#     insert('=A1+B1', 'C1',wks)
#     temp2 = wks.cell(1, 3).value
#     assert temp2 == '4'

#     wks.cell(1, 1).value = 2
#     wks.cell(2, 1).value = 2
#     insert('=A1+B1','none', wks)
#     temp2 = wks.cell(1, 3).value
#     assert temp2 == '4'

#     wks.cell(1, 1).value = 2
#     wks.cell(1, 2).value = 2
#     insert('=A1+A2','none', wks)
#     temp2 = wks.cell(1, 3).value
#     assert temp2 == '4'

#     wks.cell(1, 1).value = 2
#     wks.cell(2, 2).value = 2
#     insert('=A1+B2','none', wks)
#     temp2 = wks.cell(2, 3).value
#     assert temp2 == None

# # test_move()