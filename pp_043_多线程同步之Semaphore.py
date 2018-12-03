import random
import time
from threading import Semaphore, Thread

sem = Semaphore(3)


class MyThread(Thread):
    def run(self):
        # sem.acquire()
        with sem:
            print('%s获得资源' % self.name)
            time.sleep(random.random() * 2)
            print('%s释放资源' % self.name)
        # sem.release()


for i in range(10):
    MyThread().start()

"""
Thread-1获得资源
Thread-2获得资源
Thread-3获得资源
Thread-3释放资源
Thread-4获得资源
Thread-2释放资源
Thread-5获得资源
Thread-1释放资源
Thread-6获得资源
Thread-4释放资源
Thread-7获得资源
Thread-7释放资源
Thread-8获得资源
Thread-5释放资源
Thread-9获得资源
Thread-8释放资源
Thread-10获得资源
Thread-6释放资源
Thread-10释放资源
Thread-9释放资源
"""

"""
小结

标准库模块 threading 中提供了一个类对象 Semaphore，用于表示信号量。
它可以帮助我们控制并发线程的最大数量，从而实现多线程之间的同步。

信号量 Semaphore 也遵守了上下文管理协议，可以使用 with 语句进行简化。
"""
