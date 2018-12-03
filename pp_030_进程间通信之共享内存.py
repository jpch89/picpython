from multiprocessing import Process, Value, Array, freeze_support
import ctypes


def do_sth(num, arr):
    num.value = 1.8
    for i in range(len(arr)):
        arr[i] = -arr[i]


if __name__ == '__main__':
    # 如果要生成可执行文件，需要这一句
    freeze_support()

    # 在共享内存中创建一个表示数值的 ctypes 对象
    num = Value('d', 2.3)
    # 与上面等价
    # num = Value(ctypes.c_float, 2.3)

    # 在共享内存中创建一个表示数组的 ctypes 对象
    arr = Array('i', range(1, 5))
    # 与上面等价
    # arr = Array(ctypes.c_int, range(1, 5))

    p = Process(target=do_sth, args=(num, arr))
    p.start()
    p.join()
    print(num.value)
    print(arr[:])
"""
1.8
[-1, -2, -3, -4]
"""

"""
如果想要实现进程之间的通信，共享内存是常见的实现方式之一。
它允许多个进程直接访问同一块内存。

共享内存中对象的类型必须是 ctypes 的。
ctypes 是与 C 语言兼容的数据类型。

标准库模块 multprocessing 中给我们提供了两个函数来创建 ctypes 对象。
一个是 Value，一个是 Array。

1. Value(typecode_or_type, *args, **kwargs)
   返回值表示一个数值。
   参数 typecode_or_type 用于指定数值的类型码或 ctypes 类型。

2. Array(typecode_or_type, size_or_initializer, lock=True)
   返回值表示一个数组。
   参数 typecode_or_type 用于指定数组中元素的类型码或 ctypes 类型。
   参数 size_or_initializer 用于指定数组的长度或者 Python 中的序列。
"""
