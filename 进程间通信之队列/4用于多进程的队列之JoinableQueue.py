
"""用于多进程的队列之JoinableQueue"""

"""
    JoinableQueue是Queue的子类，添加了如下两个方法：
（1）task_done()
    在队列执行出队操作并处理完相应的任务后，执行该方法，以告知队列"任务已完成"。
（2）join()
    当前进程被阻塞，直到队列中的所有对象都已经出队并且调用了方法task_done()，也就是说，
直到所有任务都已完成，当前进程再从被阻塞的地方继续执行。
"""
from multiprocessing import Process, JoinableQueue
import time

def dequeue(jq):
    for i in range(3):
        print('出队：%s' % jq.get(True))
        print('处理相应的任务')
        time.sleep(2)
        jq.task_done()

jq = JoinableQueue()

jq.put('obj1')
jq.put('obj2')
jq.put('obj3')

mp = Process(target=dequeue, args=(jq,))
mp.start()

jq.join()

print('所有任务都已完成')