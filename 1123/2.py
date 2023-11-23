'''
題目：2
請寫Python程式，印出本課程18週上課的所有日期。
即依序下列格式顯示下列日期:
'''

import datetime


deltaofTime = datetime.timedelta(days = 7)

for 上課次數 in range(18):
    dayofFirstclass = datetime.datetime(2023, 9, 14, 13, 0, 0)
    dayofClasses = dayofFirstclass + deltaofTime*上課次數
    print(f"{dayofClasses.year}-{dayofClasses.month:02d}{dayofClasses.day:02d}")
