import pandas as pd
import os

# reading data
csvFile = r'\\conoco.net\ho_shared\L48 GIS Secure\Land\mherring\automation\python\ndic_daily_permits\csv\dr02062.csv'
csv = pd.read_csv(csvFile)
csv.head(8)
