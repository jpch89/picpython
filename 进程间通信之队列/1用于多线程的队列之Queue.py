
"""用于多线程的队列之Queue"""

"""
    为了在多线程中应用队列这种数据结构，标准库模块queue中提供了三个类对象：
（1）Queue
    与模块multiprocessing中的JoinableQueue几乎是相同的，其特点也是"先进先出"。
（2）LifoQueue
    特点是Lifo（Last in first out，后进先出），也就是说，入队和出队都是在队尾。
    后进先出的队列其实就是栈。
（3）PriorityQueue
    队列中的每个对象都有优先级。出队时选择优先级最小的对象。
    
    这三种队列的区别仅仅在于它们出队的顺序。
    
    这三种队列都是多线程安全的，都实现了所有需要的同步机制。
"""
from threading import Thread
from queue import Queue
import time

def dequeue(q):
    for i in range(3):
        print('出队：%s' % q.get(True))
        print('处理相应的任务')
        time.sleep(2)
        q.task_done()

q = Queue()

q.put('obj1')
q.put('obj2')
q.put('obj3')

mp = Thread(target=dequeue, args=(q,))
mp.start()

q.join()

print('所有任务都已完成')