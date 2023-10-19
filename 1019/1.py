total = 0   # 初始化總計值
i = 0       # 初始化加總次數

while i < 5:                                        # 開始 While 迴圈，直到 i 超過 5
    num = int(input("Please enter an integer: "))   # 提示使用者輸入要計算的五個數字
    total += num                                    # 不斷地將輸入的num值與total加總
    i += 1                                          # 將加總次數設定為i+1

    # i達到4，意思是已經加總5次
print("The sum of the five numbers is: ", total)   # 輸出加總值




'''
Output:
  Please enter an integer: 5
  Please enter an integer: 6
  Please enter an integer: 7
  Please enter an integer: 8
  Please enter an integer: 9
  
  The sum of the five numbers is:  35
'''
