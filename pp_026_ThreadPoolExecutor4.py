from concurrent.futures import ThreadPoolExecutor, as_completed
import time, random


def do_sth(i):
    time.sleep(random.random() * 2)
    return i * i


if __name__ == '__main__':
    tpe = ThreadPoolExecutor(3)

    objs = [tpe.submit(do_sth, i) for i in range(1, 5)]
    future_iterator = as_completed(objs)  # 个人理解：as 为当，整体意思是当完成的时候
    for future in future_iterator:
        print(future.result())
"""
1
9
16
4
"""

"""
小结
标准库模块 concurrent.futures 还提供了两个函数：
wait() 和 as_completed()

as_completed(fs, timeout=None):
该函数用于将指定的 Future 实例对象序列转换为迭代器。
当序列中的任意一个 Future 实例对象已经完成或者已被取消时，都会被 yield。
这样通过遍历迭代器，就可以在任意一个 Future 实例对象已经完成或者已被取消时，
立即做一些处理，比如调用 result() 来得到执行结果。

参数 fs 用于指定 Future 实例对象序列。
参数 timeout 用于指定超时时间。如果不指定（默认为 None），则不会超时。

该函数的返回值是一个 Future 实例对象的迭代器。
"""
