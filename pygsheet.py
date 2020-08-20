import sys
import time
import datetime
import gspread
import json

with open('setting.json', 'r', encoding = 'utf8') as jfile:
    setting = json.load(jfile)

def initiation():
    googleCloud = gspread.service_account(filename = 'pygsheetKey.json')
    gSheet = googleCloud.open_by_key(setting['First_Page'])
    workSheet = gSheet.sheet1
    #get = workSheet.get_all_records()
    #print(get)

initiation()
