import gspread
from gspread_formatting import *
from string import ascii_lowercase
import re

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


def delete(cell, worksheet):
    # check if cell is valid
    if cell[0].isalpha() and cell[-1].isnumeric():
        worksheet.update(cell, '')
    else:
        print("Delete: Invalid input", end="; ")


# Functionality: Move and maintain current value/formula into new cell. This means, if formula says =A3+B3, it should stay =A3+B3 when moved
def move(old_cell, new_cell, worksheet):
    # grab formula or value
    value = worksheet.acell(old_cell, value_render_option='FORMULA').value
    worksheet.update(new_cell, value, value_input_option='USER_ENTERED')
    worksheet.update(old_cell, '')

# Functionality: Bold a cell
def bold(target_cell, worksheet):
    cell_format = CellFormat(textFormat=TextFormat(bold=True))
    format_cell_range(worksheet, target_cell, cell_format)

# Functionality: Fit a column by wrapping text
def fit_column_wrap(column, worksheet):
     worksheet.format(f'{column}:{column}', {'wrapStrategy': 'WRAP'})

# Functionality: Switch the values from the one cell to another. 
def switch(cell1, cell2, worksheet):
    # get values
    value1 = worksheet.acell(cell1, value_render_option='FORMULA').value
    value2 = worksheet.acell(cell2, value_render_option='FORMULA').value

    # switch values
    worksheet.update(cell1, value2)
    worksheet.update(cell2, value1)
