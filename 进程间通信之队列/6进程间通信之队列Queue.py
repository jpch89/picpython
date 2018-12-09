
"""进程间通信之队列Queue"""

"""
    如果想要实现进程之间的通信，队列是常见的实现方式之一。
    本节示例使用的队列是Queue。
    《图解Python》
"""
from multiprocessing import Process, Queue
import os, time, random

# 写数据的子进程执行的代码
def write(q):
    print('写数据的子进程%d启动' % os.getpid())

    for obj in list(range(1, 10)):
        print('写数据：%s' % obj)
        q.put(obj, True)
        time.sleep(random.random() * 3)

    print('写数据：None')
    q.put(None, True)

    print('写数据的子进程%d结束' % os.getpid())

# 读数据的子进程执行的代码
def read(q):
    print('读数据的子进程%d启动' % os.getpid())

    while True:
        item = q.get(True)
        if item is None:
            print('读数据：None')
            break
        print('读数据：%s' % item)
        time.sleep(random.random() * 3)

    print('读数据的子进程%d结束' % os.getpid())

print('父进程%d启动' % os.getpid())

q = Queue()

pw = Process(target=write, args=(q,))
pr = Process(target=read, args=(q,))

pw.start()
pr.start()

pw.join()
pr.join()

print('父进程%d结束' % os.getpid())