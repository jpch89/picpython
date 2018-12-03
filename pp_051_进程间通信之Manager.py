from multiprocessing import Process, Manager


def f(d, l):
    d[1] = 18
    d['2'] = 56
    l.reverse()


if __name__ == '__main__':
    manager = Manager()
    # 通过 Manager 创建一个用于进程间通信的字典
    d = manager.dict()
    # 通过 Manager 创建一个用于进程间通信的列表
    l = manager.list(range(5))

    p = Process(target=f, args=(d, l))
    p.start()
    p.join()

    print(d)
    print(l)

"""
{1: 18, '2': 56}
[4, 3, 2, 1, 0]
"""

"""
如果想要实现进程间通信，Manager 也是常见的实现方式之一。
与共享内存相比，Manager 更加灵活，因为它可以支持多种对象类型。
比如字典、列表、Lock、RLock、Condition、Event、Queue 等等。
此外 Manager 还可以通过网络被不同计算机上的进程所共享。
缺点是速度比共享内存要慢。
"""
