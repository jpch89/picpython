from concurrent.futures import ThreadPoolExecutor, wait, FIRST_COMPLETED
import time, random


def do_sth(i):
    time.sleep(random.random() * 2)
    return i * i


if __name__ == '__main__':
    tpe = ThreadPoolExecutor(3)

    # objs = []
    # for i in range(1, 5):
    #     future = tpe.submit(do_sth, i)
    #     objs.append(future)

    # 我的写法：一句搞定
    objs = [tpe.submit(do_sth, i) for i in range(1, 5)]

    # 既然指定 return_when=ALL_COMPLETED 所以 not_done 应该是个空集合
    # done, not_done = wait(objs, return_when=ALL_COMPLETED)
    # done, not_done = wait(objs, return_when=FIRST_COMPLETED)
    done, not_done = wait(objs, return_when=FIRST_COMPLETED)
    print(done)
    print(not_done)
"""
{<Future at 0x1d98a04f0f0 state=finished returned int>}
{<Future at 0x1d989d00f98 state=running>, <Future at 0x1d98a039710 state=running>, <Future at 0x1d98a04f9e8 state=running>}
"""


"""
小结
标准库模块 concurrent.futures 还提供了两个函数：
wait() 和 as_completed()

wait(fs, timeout=None, return_when=ALL_COMPLETED)
该函数用于阻塞父进程，以等待指定的 Future 实例对象，直到满足指定的条件。
参数 fs 用于指定我们要等待的 Future 实例对象序列。（future sequence）
参数 timeout 用于指定等待的最长时间。如果不指定（默认为 None），则一直等待。
参数 return_when 用于指定函数何时返回，有三种取值：
FIRST_COMPLETED 当第一个实例对象已经完成或者已被取消时, 
FIRST_EXCEPTION 当第一个实例对象抛出异常时, 
ALL_COMPLETED 当所有实例对象已经完成或者已被取消时。
该函数的返回值是由两个集合组成的元组。
第一个集合是已经完成或者已被取消的所有 Future 实例对象。
第二个集合包含所有没有完成，或者没有取消的所有 Future 实例对象。
"""
