import gspread
from gspread_formatting import *
from string import ascii_lowercase
import re
#from input_parser import *

# Supported Commands

# import worksheet value
# worksheet = None
# def getWorksheet(ws):
#     global worksheet
#     worksheet = ws


# Functionality: Insert value into a singular cell
# Functionality: Insert value into a singular cell
def insert(formula, cell, worksheet):
    if cell == 'none': # if no target cell specified, auto place
        start_cell, end_cell = re.findall(r"[A-Z]+\d+", formula)
        start_col, start_row = re.match(r"([A-Z]+)(\d+)", start_cell).groups()
        end_col, end_row = re.match(r"([A-Z]+)(\d+)", end_cell).groups()

        if start_col == end_col:
            # same column, update below
            end_row_num = int(end_row) + 1
            sum_cell = end_col + str(end_row_num)
            print("Range same column:", sum_cell) # testing
            worksheet.update(sum_cell, formula, value_input_option='USER_ENTERED')
        elif start_row == end_row:
            # same row, update to the right
            col_num = col_to_num(end_col) + 1
            sum_col = num_to_col(col_num)
            sum_cell = sum_col + end_row
            print("Range is row:", sum_cell) # testing
            worksheet.update(sum_cell, formula, value_input_option='USER_ENTERED')
        else:
            # different column and row, update below
            end_row_num = int(end_row) + 1
            sum_cell = end_col + str(end_row_num)
            print("Range is row/col:", sum_cell) # testing
            worksheet.update(sum_cell, formula, value_input_option='USER_ENTERED')
    else: # if target cell specified
        worksheet.update(cell, formula, value_input_option='USER_ENTERED')




# Functionality: Delete value within a singular cell
def delete(cell):
    worksheet.update(cell, '')


# Functionality: Update cell with new_value
def edit_cell(new_value, cell):
    worksheet.update(cell, new_value)


# Functionality: Move and maintain current value/formula into new cell. This means, if formula says =A3+B3, it should stay =A3+B3 when moved
def move(old_cell, new_cell):
    # grab formula or value
    value = worksheet.acell(old_cell, value_render_option='FORMULA').value
    worksheet.update(new_cell, value, value_input_option='USER_ENTERED')
    worksheet.update(old_cell, '')

# Functionality: Bold a cell
def bold(target_cell):
    cell_format = CellFormat(textFormat=TextFormat(bold=True))
    format_cell_range(worksheet, target_cell, cell_format)

# Functionality: Fit a column by wrapping text
def fit_column_wrap(column):
    worksheet.format(f'{column}:{column}', {'wrapStrategy': 'WRAP'})

# support function for sum
def col_to_num(col):
    num = 0
    for c in col:
        num = num * 26 + (ord(c) - ord('A') + 1)
    return num

def num_to_col(num):
    col = ""
    while num > 0:
        remainder = (num - 1) % 26
        col = chr(ord('A') + remainder) + col
        num = (num - 1) // 26
    return col


# Functionality: Sums the values between the starting_cell and the end_cell inclusive. The sum goes one cell below the end_cell.
def sum(start_cell, end_cell):
    # *** INPUT CHECKS ***
    # if equivalent, just pass
    if start_cell == end_cell:
        return
    
    # if cell doesn't have number ending
    if start_cell[-1].isalpha() or end_cell[-1].isalpha():
        return
    
    # if cell doesn't have alphabet starting
    if start_cell[0].isnumeric() or end_cell[0].isnumeric():
        return

    # convert cell references to uppercase
    start_cell = start_cell.upper()
    end_cell = end_cell.upper()

    # formula to put into sum cell
    formula = f'=SUM({start_cell}:{end_cell})'
    
    # place sum in correct spot
    start_col, start_row = re.match(r"([A-Z]+)(\d+)", start_cell).groups()
    end_col, end_row = re.match(r"([A-Z]+)(\d+)", end_cell).groups()

    if start_col == end_col:
        # same column, update below
        end_row_num = int(end_row) + 1
        sum_cell = end_col + str(end_row_num)
        print("sum cell in same column:", sum_cell) # testing
        worksheet.update(sum_cell, formula, value_input_option='USER_ENTERED')
    elif start_row == end_row:
        # same row, update to the right
        col_num = col_to_num(end_col) + 1
        sum_col = num_to_col(col_num)
        sum_cell = sum_col + end_row
        print("sum cell to the right:", sum_cell) # testing
        worksheet.update(sum_cell, formula, value_input_option='USER_ENTERED')
    else:
        # different column and row, update below
        end_row_num = int(end_row) + 1
        sum_cell = end_col + str(end_row_num)
        print("sum cell in different row and column:", sum_cell) # testing
        worksheet.update(sum_cell, formula, value_input_option='USER_ENTERED')
    
    # for c in range(len(end_cell)):
    #     if start_cell[c] == end_cell[c]:
    #         if start_cell[c+1].isnumeric() and end_cell[c+1].isnumeric(): # must be same column so update below
    #             end_cell_num = int(end_cell[c+1:]) + 1
    #             sum_cell = end_cell[0:c+1] + str(end_cell_num)
    #             print("sum cell in same column:", sum_cell)
    #             # worksheet.update(sum_cell, formula, value_input_option='USER_ENTERED')
    #             return
    #     elif (start_cell[-c-1] == end_cell[-c-1]): # must be different columns, so test for same row
    #         if start_cell[-c-2].isalpha() and end_cell[-c-2].isalpha():
    #             # update code so that it will create string that says the next cell to the right. For example. Z5 becomes AA5. 
    #             print("same row", start_cell, end_cell)
    #             return
    #     else: # must be different column and row, which in that case, just put below 
    #         for j in range(len(end_cell)):
    #             if end_cell[j].isnumeric():
    #                 end_cell_num = int(end_cell[j:]) + 1
    #                 sum_cell = end_cell[0:j] + str(end_cell_num)
    #                 print("sum cell in different row and column:", sum_cell)
    #                 # worksheet.update()
    #                 return        

    # worksheet.update(f"{end_cell_row+1}", formula, value_input_option='USER_ENTERED')


# Functionality: Sums the values between the starting_cell and the end_cell inclusive. The sum goes into the target cell.
def target_sum(start_cell, end_cell, target_cell):
    # *** INPUT CHECKS ***
    # if equivalent, just pass
    if start_cell == end_cell:
        return
    
    # if cell doesn't have number ending
    if start_cell[-1].isalpha() or end_cell[-1].isalpha():
        return
    
    # if cell doesn't have alphabet starting
    if start_cell[0].isnumeric() or end_cell[0].isnumeric():
        return

    # formula to put into sum cell
    formula = f'=SUM({start_cell}:{end_cell})'
    worksheet.update(target_cell, formula, value_input_option='USER_ENTERED')


# Functionality: Switch the values from the one cell to another. 
def switch(cell1, cell2):
    # get values
    value1 = worksheet.acell(cell1, value_render_option='FORMULA').value
    value2 = worksheet.acell(cell2, value_render_option='FORMULA').value

    # switch values
    worksheet.update(cell1, value2)
    worksheet.update(cell2, value1)


# Functionality: Averages the values between the starting_cell and the end_cell inclusive. The average goes one cell below the end_cell.
def average(start_cell, end_cell):
    pass


# Functionality: Counts the number of values in a range of cells. (Basically is it a number)
def count(start_cell, end_cell):
    pass


# Functionality: Finds the max value in a range of cells
def max(start_cell, end_cell):
    pass


# Functionality: Finds the min value in a range of cells
def min(start_cell, end_cell):
    pass


# Functionality: Sort by prioritizing numerical order and then alphabetical order. Range must be specified
def sort(start_cell, end_cell):
    pass


# Functionality: Create the filter bar on the specified range.
def add_filter(start_cell, end_cell):
    pass


# Functionality: Count the occurences of a certain value (or string) in a data range
def occurrences(value, start_cell, end_cell):
    pass


# MORE COMMANDS TO BE ADDED LATER FOR COMPLEX DATA ANALYTICS SUCH AS MAKING CHARTS, REGRESSIONS, TRENDLINES.