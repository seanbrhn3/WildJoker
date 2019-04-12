from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from pprint import pprint

from googleapiclient import discovery
# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/spreadsheets'
#https://docs.google.com/spreadsheets/d/1sMXpRIQhO1_COatlez0RTvaioIqXD5TM5NCMOTDIqLQ/edit?usp=sharing
# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1KVCzNbMt1U_cAUeSUw8Q_pExWDl89kDcmuMv38-5Fac'
SAMPLE_RANGE_NAME = 'Class Data!A2:E'
class Spreadsheet(object):
    entries = {}
    count = 1
    def add_values_google(self,values):
        store = file.Storage('token.json')
        creds = store.get()
        if not creds or creds.invalid:
            flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
            creds = tools.run_flow(flow, store)
        service = build('sheets', 'v4', http=creds.authorize(Http()))



        # The ID of the spreadsheet to update.
        spreadsheet_id = '1KVCzNbMt1U_cAUeSUw8Q_pExWDl89kDcmuMv38-5Fac'  # TODO: Update placeholder value.

        # The A1 notation of a range to search for a logical table of data.
        # Values will be appended after the last row of the table.
        range_ = 'Sheet1!A1'  # TODO: Update placeholder value.

        # How the input data should be interpreted.
        value_input_option = 'RAW'  # TODO: Update placeholder value.

        # How the input data should be inserted.
        insert_data_option = 'INSERT_ROWS'  # TODO: Update placeholder value.
        vals = []
        vals.append(values['joke'])
        value_range_body = {
            # TODO: Add desired entries to the request body.
            "values" : [vals]
        }

        request = service.spreadsheets().values().append(spreadsheetId=spreadsheet_id, range=range_, valueInputOption=value_input_option, insertDataOption=insert_data_option, body=value_range_body)
        response = request.execute()

        pprint(response)
    def add_values_amazon(self,values):
        store = file.Storage('token.json')
        creds = store.get()
        if not creds or creds.invalid:
            flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
            creds = tools.run_flow(flow, store)
        service = build('sheets', 'v4', http=creds.authorize(Http()))



        # The ID of the spreadsheet to update.
        spreadsheet_id = '1SCfXHW0rzOl_WCJbIICV4uAiF39Ze6o_j095Ns2Oz7s'  # TODO: Update placeholder value.

        # The A1 notation of a range to search for a logical table of data.
        # Values will be appended after the last row of the table.
        range_ = 'Sheet1!A1'  # TODO: Update placeholder value.

        # How the input data should be interpreted.
        value_input_option = 'RAW'  # TODO: Update placeholder value.

        # How the input data should be inserted.
        insert_data_option = 'INSERT_ROWS'  # TODO: Update placeholder value.
        vals = []
        vals.append(values['joke'])
        value_range_body = {
            # TODO: Add desired entries to the request body.
            "values" : [vals]
        }

        request = service.spreadsheets().values().append(spreadsheetId=spreadsheet_id, range=range_, valueInputOption=value_input_option, insertDataOption=insert_data_option, body=value_range_body)
        response = request.execute()

        pprint(response)
