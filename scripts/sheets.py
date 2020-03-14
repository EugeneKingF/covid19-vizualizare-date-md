import gspread
from oauth2client.service_account import ServiceAccountCredentials


class SheetReader:
    def __init__(self):
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name('covid_MD-139a65d546ca.json', scope)
        self.client = gspread.authorize(creds)

    def getAllSheetDataRaw(self, name):
        sheet = self.client.open(name).sheet1
        covid = sheet.get_all_records()
        return covid

    def getAllSheetDataForPlot(self, name):
        data = self.getAllSheetDataRaw(name)
        for i in data:
            i["data"] = i["data"] + " " + i["ora"]
        return data

# x = SheetReader()
#
# data = x.getAllSheetDataRaw("covid")
#
#
#
# print(data)



