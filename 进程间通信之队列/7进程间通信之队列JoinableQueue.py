
"""进程间通信之队列JoinableQueue"""

"""
    如果想要实现进程之间的通信，队列是常见的实现方式之一。
    本节示例使用的队列是JoinableQueue。
"""
from multiprocessing import Process, JoinableQueue
import os, time, random

# 写数据的子进程执行的代码
def write(jq):
    print('写数据的子进程%d启动' % os.getpid())

    for obj in list(range(1, 10)):
        print('写数据：%s' % obj)
        jq.put(obj, True)
        time.sleep(random.random() * 3)

    print('写数据：None')
    jq.put(None, True)

    # 写数据的子进程被阻塞
    # 所有对象都已经出队并且调用了方法task_done()之后，写数据的子进程再从被阻塞的地方继续执行
    jq.join()

    print('写数据的子进程%d结束' % os.getpid())

# 读数据的子进程执行的代码
def read(jq):
    print('读数据的子进程%d启动' % os.getpid())

    while True:
        item = jq.get(True)
        if item is None:
            print('读数据：None')
            jq.task_done()
            break
        print('读数据：%s' % item)
        time.sleep(random.random() * 3)
        jq.task_done()

    print('读数据的子进程%d结束' % os.getpid())

print('父进程%d启动' % os.getpid())

jq = JoinableQueue()

pw = Process(target=write, args=(jq,))
pr = Process(target=read, args=(jq,))

pw.start()
pr.start()

pw.join()
pr.join()

print('父进程%d结束' % os.getpid())