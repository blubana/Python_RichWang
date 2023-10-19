import random

while True:
    n = int(input("請輸入數字(>5): "))  # 提示使用者設定名為n的整數，作為list的數字個數

    list = random.sample(range(100), n)  # 生成一個長度為n的list，其中的元素是0到99之間的隨機整數
    print(f"list = {list}")  # 列印出生成的list


'''
Output:
請輸入數字(>5): 10
list = [38, 63, 60, 64, 98, 58, 76, 36, 92, 49]
'''
