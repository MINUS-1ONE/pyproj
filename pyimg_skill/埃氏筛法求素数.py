# -*- coding: utf-8 -*-

def _odd_iter():
	# 生成奇数 因为偶数是2的倍数不可能是素数 先筛去
    n = 1
    while True:
        n = n + 2
        yield n
        
def _not_divisible(n):
    return lambda x: x % n > 0 # x是怎么来的？？？  解答:return lambda x:x % n > 0 实则返回一个函数
                               # 相当于返回一个 g(x)：x%n>0（这里很重要 是返回一个函数） ，因此下面的primes代码中的it = filter(_not_divisible(n), it)
                               #相当于把it中的每一个元素放入g(x)里去检测True or False
def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 过滤掉所有其倍数筛去素数 构造新序列

# 打印1000以内的素数:
for n in primes():
    if n < 1000:
        print(n,end = ' ')
    else:
        break        