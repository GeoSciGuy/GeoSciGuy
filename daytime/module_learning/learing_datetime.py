import datetime

pdf_url = r'https://www.dmr.nd.gov/oilgas/daily/2023/'
x = datetime.datetime.now()
print(x)

print((x.strftime('%m')),(x.strftime('%d')), ((x.strftime('%y'))))
now = datetime.datetime.now()
month = x.strftime('%m')
day = x.strftime('%d')
year = x.strftime('%y')
today = now.strftime("%Y-%m-%d")
yesterday = (now + datetime.timedelta(days=-1)).strftime("%d")
today_fn = "dr" + month + day + year + ".pdf"
yesterday_fn = "dr" + month + yesterday + year + ".pdf"


print(today_fn)
print(yesterday_fn)
print(pdf_url + today_fn)
print(pdf_url + yesterday_fn)