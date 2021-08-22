import gspread
from oauth2client.service_account import ServiceAccountCredentials

import const

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('.data/gcpkey.json')

gc = gspread.authorize(credentials)
SPREADSHEET_KEY = const.SPREADSHEET_KEY


def sheet_setup(sheetname: str):
    workbook = gc.open_by_key(SPREADSHEET_KEY)
    worksheet = workbook.worksheet(sheetname)
    return worksheet
