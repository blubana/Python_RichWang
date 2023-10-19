num = int(input("請輸入數字(1~9):"))  # 提示使用者輸入數字

for i in range(num, 0, -1):  # 開始for迴圈，從num到1

    for j in range(1, i):  # 開始內部for迴圈，從1到i
        print(" ", end="")  # 列印空格

    for k in range(i, num+1):  # 開始內部for迴圈，從i到num+1
        print(k, end="")  # 列印數字

    print()  # 換行

'''
Output:
請輸入數字(1~9):8
       8
      78
     678
    5678
   45678
  345678
 2345678
12345678
'''
