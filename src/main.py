from credsGoogleSheetsApi import ConnectGoogleSheetsApi

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

conn = ConnectGoogleSheetsApi()
conn.connect()

def getSheetsValues(conn):
    try:
        service = build('sheets', 'v4', credentials=conn.creds)
        sheet = service.spreadsheets()
        result = (sheet.values().get(spreadsheetId="1dkKQhT6rHWm8Xvz-qN9B9zm3kspugkUYceU8qACDJHI", range="DB1!A1:F82").execute())
        return result

    except HttpError as err:
        print(err)

