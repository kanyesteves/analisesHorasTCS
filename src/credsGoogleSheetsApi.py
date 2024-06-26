import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow


class ConnectGoogleSheetsApi():
    def __init__(self):
        self.creds = None
        self.SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

    def connect(self):
        if os.path.exists("token.json"):
            self.creds = Credentials.from_authorized_user_file("token.json", self.SCOPES)

        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file("credentials.json", self.SCOPES)
                self.creds = flow.run_local_server(port=8501)
                
            with open("token.json", "w") as token:
                token.write(self.creds.to_json())
