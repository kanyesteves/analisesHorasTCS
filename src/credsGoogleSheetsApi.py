import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]
SAMPLE_SPREADSHEET_ID = "1dkKQhT6rHWm8Xvz-qN9B9zm3kspugkUYceU8qACDJHI"
SAMPLE_RANGE_NAME = "DB1!A1:F82"


class ConnectGoogleSheetsApi():
    def __init__(self):
        self.creds = ""

    def connect(self):
        self.creds = None
        if os.path.exists("token.json"):
            self.creds = Credentials.from_authorized_user_file("token.json", SCOPES)

        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    "credentials.json", SCOPES
                )
                self.creds = flow.run_local_server(port=0)
                
            with open("token.json", "w") as token:
                token.write(self.creds.to_json())
