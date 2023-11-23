'''
題目：1
請寫Python程式，使用 datetime，來印出今天是民國幾年幾月幾日星期幾? 
'''
import datetime

now = datetime.datetime.now()

now_year_mingguo = now.year - 1911  #   民國年

days = "一二三四五六日"             #   定義 now.weekday 輸出的數字對應的中文
Index = now.weekday()              #   建立 Index 儲存 now.weekday 輸出的數字 
now_weekday = "星期"+days[Index]    #   儲存 now.weekday 輸出的數字對應的中文

print(f"今天是民國{now_year_mingguo}年{now.month}月{now.day}日，是{now_weekday}")

#print(f"星期{days[Index]}")


