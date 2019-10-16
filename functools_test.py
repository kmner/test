# 10.2. functools — Higher-order functions and operations on callable objects

import functools
import locale
from urllib import request

# functools.cmp_to_key(func) 转换旧的key函数为新函数
d = sorted('ABCDEFG', key=functools.cmp_to_key(locale.strcoll))
print(d)

#  LRU (least recently used) cache
@functools.lru_cache(maxsize=32)
def get_pep(num):
    'Retrieve text of a Python Enhancement Proposal'
    resource = 'http://www.python.org/dev/peps/pep-%04d/' % num
    try:
        with request.urlopen(resource) as s:
            return s.read()
    except Exception:
        return 'Not Found'

#for n in 8, 290, 308, 320, 8, 218, 320, 279, 289, 320, 9991:
for n in 8, 290:
    pep = get_pep(n)
    print(n, len(pep))

print(get_pep.cache_info())


# 排序比较。

# 提供__lt__(), __le__(), __gt__(), or __ge__()之一。
# 再提供__eq__() 方法
@functools.total_ordering
class Student:
    def _is_valid_operand(self, other):
        return (hasattr(other, "lastname") and
                hasattr(other, "firstname"))
    def __eq__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        return ((self.lastname.lower(), self.firstname.lower()) ==
                (other.lastname.lower(), other.firstname.lower()))
    def __lt__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        return ((self.lastname.lower(), self.firstname.lower()) <
                (other.lastname.lower(), other.firstname.lower()))


# functools.partial(func, *args, **keywords)
basetwo = functools.partial(int, base=2)
basetwo.__doc__ = 'Convert base 2 string to an int.'
print(basetwo('10010'))


# class functools.partialmethod(func, *args, **keywords)
# partialmethod 设计用于方法定义
class Cell(object):
    def __init__(self):
        self._alive = False
    @property
    def alive(self):
        return self._alive
    def set_state(self, state):
        self._alive = bool(state)
    set_alive = functools.partialmethod(set_state, True)
    set_dead = functools.partialmethod(set_state, False)

c = Cell()
print(c.alive)
c.set_alive()
print(c.alive)


# functools.reduce(function, iterable[, initializer])
# 累加
# reduce 减少; 缩小; 使还原; 使变弱;
# 此处是累加的意思
d= functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5],100)
print(d)


# 函数重载
@functools.singledispatch
def fun(arg, verbose=False):
    if verbose:
        print("Let me just say,", end=" ")
    print(arg)

@fun.register(int)
def _(arg, verbose=False):
    if verbose:
        print("Strength in numbers, eh?", end=" ")
    print(arg)

@fun.register(list)
def _(arg, verbose=False):
    if verbose:
        print("Enumerate this:")
    for i, elem in enumerate(arg):
        print(i, elem)

print('函数重载')
fun("test.", verbose=True)
fun(42, verbose=True)
fun(['spam', 'spam', 'eggs', 'spam'], verbose=True)
fun({'a':'txt','b':'dat'}, verbose=True)

'''
函数重载
Let me just say, test.
Strength in numbers, eh? 42
Enumerate this:
0 spam
1 spam
2 eggs
3 spam
Let me just say, {'b': 'dat', 'a': 'txt'}
'''

# 默认partial对象没有__name__和__doc__, 这种情况下，
# 对于装饰器函数非常难以debug.使用update_wrapper(),
# 从原始对象拷贝或加入现有partial对象

# 它可以把被封装函数的__name__、 module 、__doc__和 __dict__
# 都复制到封装函数去(模块级别常量WRAPPER_ASSIGNMENTS, WRAPPER_UPDATES)

# 缺省是模块级别常量 WRAPPER_ASSIGNMENTS
# 赋给包装器__module__, __name__, __qualname__, __annotations__ 和 __doc__

# WRAPPER_UPDATES 更像包装器的__dict__

# functools.update_wrapper(wrapper, wrapped, assigned=WRAPPER_ASSIGNMENTS, updated=WRAPPER_UPDATES)
# 更新包装器函数以便更像被包装的函数
from functools import update_wrapper
def wrap2(func):
    def call_it(*args, **kwargs):
        """wrap func: call_it2"""
        print('before call')
        return func(*args, **kwargs)
    return update_wrapper(call_it, func)

@wrap2
def hello2():
    """test hello"""
    print('hello world2')

hello2()
print(hello2.__name__)
print(hello2.__doc__)


print("#####################")

# @functools.wraps(wrapped, assigned=WRAPPER_ASSIGNMENTS, updated=WRAPPER_UPDATES)
from functools import wraps
def my_decorator(f):
    @wraps(f)
    def wrapper(*args, **kwds):
        print('Calling decorated function')
        return f(*args, **kwds)
    return wrapper

@my_decorator
def example():
    """Docstring"""
    print('Called example function')

example()
print(example.__name__)
print(example.__doc__)