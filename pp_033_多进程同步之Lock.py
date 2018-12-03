"""
标准库模块 multiprocessing 中提供了一个类对象 Lock，用于表示锁。
用于实现多进程之间的同步。
简单地说，同步就意味着阻塞和等待。

类对象 Lock 提供了两个用于获得锁和释放锁的方法，分别是 aquire 和 release。
为了保证获得锁的进程用完后一定要释放锁，可以将操作共享数据的相关代码放在 try 语句块中。
把释放锁的代码放在 finally 语句块中。
类对象 Lock 遵守了上下文管理协议，所以可以使用 with 语句带代替 try/finally。
"""

from multiprocessing import Process, Lock, Value

num = Value('i', 0)


def do_sth(num, lock):
    for i in range(10000):
        """
        lock.acquire()
        try:
            num += 1
        finally:
            lock.release() 
        """
        with lock:
            num.value += 1


if __name__ == '__main__':
    lock = Lock()

    p1 = Process(target=do_sth, args=(num, lock))
    p2 = Process(target=do_sth, args=(num, lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print(num.value)
