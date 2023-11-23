'''題目：5
請寫一個Python程式，完成 Hanoi tower 的搬移函式寫作。
def hanoi(n, a, b, c)
可以將 n 個盤子，從柱子 a，藉由輔助柱 b 的協助，將 n 個盤子搬移到柱子 c。
最後請列出 Hanoi tower 搬移三個盤子的所有過程。
'''

'''
解題思路:
| No. |               想法              |      舉例      |
| 1.  |  每次只解決最上層的兩個盤子       |  最上層兩盤A,B  |
| 2.  |  把最上層的盤子移到最右邊         |  把A移到最右邊  |
| 3.  |  把上往下數的第二個盤子移到中間   |  把B移到中間    |
| 4.  |  把最右邊(最上層)的盤子移到中間   |  把A移到中間    |
'''


def hanoi(n, a, b, c):
    if n == 1:
        print(f"把第{n}個盤子從{a}移到{c}")
        return

    else:
        hanoi( n - 1, a, c, b)
        print(f"把第{n}個盤子從{a}移到{c}")
        hanoi( n - 1, b, a, c)

hanoi(3, "a", "b", "c")
