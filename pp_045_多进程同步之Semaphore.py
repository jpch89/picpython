from multiprocessing import Semaphore, Process
import time, random


class MyProcess(Process):
    def __init__(self, sem, *args, **kwargs):
        self.sem = sem
        super().__init__(*args, **kwargs)

    def run(self):
        with self.sem:
            print('%s获得资源' % self.name)
            time.sleep(random.random() * 10)
            print('%s释放资源' % self.name)


if __name__ == '__main__':
    sem = Semaphore(3)
    for i in range(10):
        MyProcess(sem).start()

"""
MyProcess-1获得资源
MyProcess-2获得资源
MyProcess-4获得资源
MyProcess-1释放资源
MyProcess-3获得资源
MyProcess-4释放资源
MyProcess-5获得资源
MyProcess-5释放资源
MyProcess-8获得资源
MyProcess-2释放资源
MyProcess-7获得资源
MyProcess-7释放资源
MyProcess-6获得资源
MyProcess-3释放资源
MyProcess-9获得资源
MyProcess-6释放资源
MyProcess-10获得资源
MyProcess-8释放资源
MyProcess-9释放资源
MyProcess-10释放资源
"""

"""
小结

标准库模块 multiprocessing 中提供了一个类对象 Semaphore，用于表示信号量。
它可以帮助我们控制并发进程的最大数量，从而实现多进程之间的同步。

信号量 Semaphore 也遵守了上下文管理协议，可以使用 with 语句进行简化。
"""
