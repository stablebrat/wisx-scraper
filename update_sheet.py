import gspread
from gspread_dataframe import set_with_dataframe
from oauth2client.service_account import ServiceAccountCredentials
import os
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

def update_google_sheet(df: pd.DataFrame):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
    client = gspread.authorize(creds)

    sheet_id = os.getenv("SHEET_ID")
    print(f"Using Sheet ID: {sheet_id}")
    sheet = client.open_by_key(sheet_id).sheet1
    print("Connected to Google Sheet")

    # Clear the sheet
    sheet.clear()

    # ✅ Properly update the sheet with the DataFrame
    set_with_dataframe(sheet, df)
    print("Data successfully written to Google Sheet")
