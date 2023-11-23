'''
題目：3
請模仿級數遞迴相加的例子，寫一個計算階乘值的遞迴函式。
其中階乘的定義: factorial(n) = n! = 1*2*...*(n-1)*n。 
'''
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(6))
