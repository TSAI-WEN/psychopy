from datetime import datetime

print"YMD?"
date=raw_input()

week=datetime.strptime(date,"%Y%m%d").weekday()

print(week)