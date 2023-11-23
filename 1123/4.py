'''
題目：4
請寫一個Python程式，使用遞迴方法計算 Fibonacci numbers。
其中 Fibonacci numbers 的生成規則定義如下: 
1) fib(0) = fib(1) = 1
2) fib(n) = fib(n-1) + fib(n-2)
即首兩項的值均為1，其後各項的值為其前兩項的和。
例如，
Fibonacci numbers: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ... 
'''

def fib(n):
    if n == 1:
        return [1]
    
    if n == 2:
        return [1, 1]
    
    fibonacci_Nums = [1, 1]
    for i in range(2, n):
        fibonacci_Nums.append(fibonacci_Nums[-1] + fibonacci_Nums[-2])

    return fibonacci_Nums
 

print (fib(10))



