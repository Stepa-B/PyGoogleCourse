import csv
import datetime
import requests
FILE_URL = "https://storage.googleapis.com/gwg-content/gic215/employees-with-date.csv"
def download_file(url):
    with requests.Session() as s:
        download = s.get(FILE_URL)
        decoded_content = download.content.decode('utf-8')
        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        prelines = list(cr)
        del prelines[0]
        lines = sorted(prelines, key=lambda x:x [3])
    return lines
print(download_file(FILE_URL))

