import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]  # noqa

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)

sheet = client.open("rpi-attendance-record").sheet1  # Open the spreadhseet

data = sheet.get_all_records()  # Get a list of all records

numRows = sheet.row_count  # Get the number of rows in the sheet

pprint(data)
