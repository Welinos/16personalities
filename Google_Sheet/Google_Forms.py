from __future__ import print_function
from googleapiclient.discovery import build
from google.oauth2 import service_account

def data_from_and_to_Google(result):
    result_to_compare = ""
    for i in range(len(result[0])-2):
        result_to_compare+=result[0][i]
    SERVICE_ACCOUNT_FILE = './Google_Sheet/keys.json'
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    creds = None
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    # The ID of a document.
    DOCUMENT_ID = '1EzGd2zk0kb65ilVv2Xtvbw1cpSUhLXxO0zAucy-Hi58'

    service = build('sheets', 'v4', credentials=creds)

    # call the sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=DOCUMENT_ID, range="Arkusz1!A1:B16").execute()
    values = result.get('values', [])  # odczytane dane

    for i in range(len(values)):
        values[i][1] = int(values[i][1])
        if(result_to_compare==values[i][0]):
            values[i][1]+=1
            break

    request = sheet.values().update(spreadsheetId=DOCUMENT_ID, range="Arkusz1!A1:B16",
                                    valueInputOption="USER_ENTERED", body={"values": values}).execute()
    return values

data_from_and_to_Google("Dowódca - ENTJ-T")

