
"""线程间通信之队列Queue"""

"""
    如果想要实现线程之间的通信，队列是常见的实现方式之一。
    本节示例使用的队列是Queue。
"""
from threading import Thread, current_thread
from queue import Queue
import time, random

# 写数据的子线程执行的代码
def write(q):
    print('写数据的子线程%s启动' % current_thread().getName())

    for obj in list(range(1, 10)):
        print('写数据：%s' % obj)
        q.put(obj, True)
        time.sleep(random.random() * 3)

    print('写数据：None')
    q.put(None, True)

    # 写数据的子线程被阻塞
    # 所有对象都已经出队并且调用了方法task_done()之后，写数据的子线程再从被阻塞的地方继续执行
    q.join()

    print('写数据的子线程%s结束' % current_thread().getName())

# 读数据的子线程执行的代码
def read(q):
    print('读数据的子线程%s启动' % current_thread().getName())

    while True:
        item = q.get(True)
        if item is None:
            print('读数据：None')
            q.task_done()
            break
        print('读数据：%s' % item)
        time.sleep(random.random() * 3)
        q.task_done()

    print('读数据的子线程%s结束' % current_thread().getName())

print('父线程%s启动' % current_thread().getName())

q = Queue()

tw = Thread(target=write, args=(q,))
tr = Thread(target=read, args=(q,))

tw.start()
tr.start()

tw.join()
tr.join()

print('父线程%s结束' % current_thread().getName())