import itertools



########## Infinite Iterators: ##########
# 数字的无限迭代
for c in itertools.count(10):
    print(c)
    if c>10:
        break

print()
# 特定字符的无限迭代
a = 0
for c in itertools.cycle('ABCD'):
    print(c)
    a += 1
    if a>10:
        break

print()
# 重复特定次数
for c in itertools.repeat('ABCD',3):
    print(c)


########## Iterators terminating on the shortest input sequence: ##########

print()
# 累积计算
for c in itertools.accumulate([1,2,3,4,5]):
    print(c)

print()
# 合并字符串
for c in itertools.chain('ABC', 'DEF'):
    print(c)

print()
# 合并字符串
for c in itertools.chain.from_iterable(['ZYX', 'UVW']) :
    print(c)

print()
# 压缩字符串
for c in itertools.compress('ABCDEF', [1,0,1,0,1,1]) :
    print(c)

print()
# 过滤字符串
# 获得第一次断言是false后的一切元素
for c in itertools.dropwhile(lambda x: x<5, [1,4,6,4,1,20,50]) :
    print(c)

print()
# 过滤字符串
# 获得断言是false的元素
for c in itertools.filterfalse(lambda x: x%2, range(10))  :
    print(c)

print()
# 只要作用于函数的两个元素返回的值相等，
# 这两个元素就被认为是在一组的，而函数返回值作为组的key。
for c,sub in itertools.groupby('AAABBBCCC', lambda c: c.upper()):
    print(c,list(sub))

print()
# seq, [start,] stop [, step]
for c in itertools.islice('ABCDEFG', 2, None):
    print(c)

print()
# func, seq
# func(*seq[0]), func(*seq[1]), ...
for c in itertools.starmap(pow, [(2,5), (3,2), (10,3)]) :
    print(c)

print()
# pred, seq
# seq[0], seq[1], until pred fails
for c in itertools.takewhile(lambda x: x<5, [1,4,6,4,1]) :
    print(c)

print()
# 一个迭代器变成n个
# it, n
# it1, it2, ... itn splits one iterator into n
for c in itertools.tee([1,4,6,4,1],2) :
    print(list(c))

print()
# 按照最长的进行组合成元组
for c in itertools.zip_longest('ABCD', 'xy', fillvalue='-'):
    print(c)


########## Combinatoric generators: ##########

print()
# 笛卡尔积
# p, q, ... [repeat=1]
for c in itertools.product('ABCD', repeat=2):
    print(c)

print()
# 返回r长度的元素的排列
# Return successive r length permutations of elements in the iterable.
# successive 逐次; 连续的，相继的; 继承的，接替的;
# permutations 序列，排列，排列中的任一组数字或文字
for c in itertools.permutations('ABCD', 2):
    print(c)

print()
# r长度的元素的组合，元素不重复
for c in itertools.combinations('ABCD', 2):
    print(c)


print()
# r长度的元素的组合，允许重复
for c in itertools.combinations_with_replacement('ABCD', 2):
    print(c)