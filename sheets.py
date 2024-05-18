import gspread
import datetime
from constants import *
import pandas
import gspread_dataframe
from rfid import *
from verify import *

# from oauth2client.service_account import ServiceAccountCredentials

gc = gspread.service_account(filename=Filename)
dt = datetime.datetime.now()

# Open a sheet from a spreadsheet in one go
wks = gc.open_by_key(Key)

current_sheet = wks.worksheet(worksheet_name)
print(current_sheet.get_all_values())

dateandtime = dt.strftime("%d-%m-%Y, %H:%M:%S")
print(dateandtime)
current_sheet.update_cell(1, 2, 'DateandtimeLogin')
current_sheet.update_cell(2, 2, dateandtime)

def updatesheet(id,check):
    if id == 389276073774:
        name = "Labdhi" 
    else:
        name = "Rachit"

    data = {"entry1":{"Name":name, "DateandTime":dateandtime, "ID":id, "Verify":check}}
            
    df = pandas.DataFrame.from_dict(data)
    current_sheet = wks.worksheet(worksheet_name)
    df = pandas.DataFrame.from_dict(data, orient='index')
    current_sheet.clear()
    gspread_dataframe.set_with_dataframe(current_sheet, df)