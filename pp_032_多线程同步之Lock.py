"""
标准库模块 threading 中提供了一个类对象 Lock，用于表示锁。
用于实现多线程之间的同步。
简单地说，同步就意味着阻塞和等待。

类对象 Lock 提供了两个用于获得锁和释放锁的方法，分别是 aquire 和 release。
为了保证获得锁的线程用完后一定要释放锁，可以将操作共享数据的相关代码放在 try 语句块中。
把释放锁的代码放在 finally 语句块中。
类对象 Lock 遵守了上下文管理协议，所以可以使用 with 语句带代替 try/finally。
"""

from threading import Thread, Lock

num = 0

lock = Lock()


def do_sth():
    global num
    for i in range(1000000):
        """
        lock.acquire()
        # 确保一定能释放锁
        try:
            num += 1
        finally:
            lock.release()
        """
        # 进入运行时上下文，自动调用 lock.acquire()
        # 来开运行时上下文，自动调用 lock.release()
        with lock:
            num += 1

t1 = Thread(target=do_sth)
t2 = Thread(target=do_sth)

t1.start()
t2.start()

t1.join()
t2.join()

print(num)
"""
2000000
"""
