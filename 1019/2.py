my_info = input("plz input your info: ")  # 引導使用者輸入my_info的值
i = 1  # 初始化i值

while i <= len(my_info):  # 開始while迴圈，直到i超過my_info的長度
    print(my_info[:i])  # 利用slicing對my_info進行切片
    i += 1  # 將i值設定為i+1


'''
Output:
  plz input your info: 測試 123456789 測試
  測   
  測試 
  測試 
  測試 1
  測試 12
  測試 123
  測試 1234
  測試 12345
  測試 123456
  測試 1234567
  測試 12345678
  測試 123456789
  測試 123456789
  測試 123456789 測
  測試 123456789 測試
  '''
