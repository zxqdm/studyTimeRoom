

# 列表推导同filter和map的比较
import timeit

TIMES = 10000

SETUP = """
symbols = '$¢£¥€¤'
def non_ascii(c):
    return c > 127
"""

def clock(label, cmd):
    res = timeit.repeat(cmd, setup=SETUP, number=TIMES)
    print(label, *('{:.3f}'.format(x) for x in res))

clock('listcomp        :', '[ord(s) for s in symbols if ord(s) > 127]')
clock('listcomp + func :', '[ord(s) for s in symbols if non_ascii(ord(s))]')
clock('filter + lambda :', 'list(filter(lambda c: c > 127, map(ord, symbols)))')
clock('filter + func   :', 'list(filter(non_ascii, map(ord, symbols)))')

# 笛卡尔积
# 笛卡尔乘积是指在数学中，两个集合X和Y的笛卡尓积（Cartesian product），又称直积，表示为X × Y，第一个对象是X的成员而第二个对象是Y的所有可能有序对的其中一个成员
li = [(color, size) for size in ["H", "M"] for color in ["blue", "yellow"]]
print(li)


# 具名元组
# 用 `namedtuple` 构建的类的实例所消耗的内存跟元组是一样的.
# 这个实例跟普通的对象实例比较会小一些, 因为python不会用 `__dict__` 存放实例的属性
from collections import namedtuple

City = namedtuple("City", "name country")
jincheng = City("JinCheng", "China")
print(jincheng)
print(jincheng.name)
print(jincheng.country)
print(jincheng[1])


# 切片
# 1.对对象进行切片

# 2.给切片赋值
# 如果赋值的对象是一个切片, 那么赋值语句的右侧必须是一个可迭代对象.
l = list(range(10))

l[2:5] = [20, 30]
print(l)

del l[5:7]
print(l)

# 会报错
# False
# l[2:5] = 100
# True
l[2:5] = [100]

# 对序列使用 `+` 和 `*`
# 不修改原有的操作对象, 而是构建一个全新的序列


# 用 `bisect` 来管理已排序的序列

# bisect
import bisect
import sys

HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]

ROW_FMT = '{0:2d} @ {1:2d}    {2}{0:<2d}'

def demo(bisect_fn):
    for needle in reversed(NEEDLES):
        position = bisect_fn(HAYSTACK, needle)  # <1>
        offset = position * '  |'  # <2>
        print(ROW_FMT.format(needle, position, offset))  # <3>

if __name__ == '__main__':

    if sys.argv[-1] == 'left':    # <4>
        bisect_fn = bisect.bisect_left
    else:
        bisect_fn = bisect.bisect

    print('DEMO:', bisect_fn.__name__)  # <5>
    print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
    demo(bisect_fn)

# insort
import bisect
import random

SIZE = 7

random.seed(1729)

my_list = []
for i in range(SIZE):
    new_item = random.randrange(SIZE*2)
    bisect.insort(my_list, new_item)
    print('%2d ->' % new_item, my_list)
