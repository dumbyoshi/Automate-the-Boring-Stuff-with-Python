import os 
import openpyxl
os.chdir('F:\Germany')
workbook = openpyxl.load_workbook('DATA SCIENCE _ NIKSHALA.xlsx')
workbook.get_sheet_names()
print(workbook.get_sheet_names())
