
"""用于多进程的队列之Queue"""

"""
    以现实生活中人们排队买票形成的队列为例，新来的人要排在队列的尾部，称之为"入队"；队列的头部
已经买完票的人从队列中离开，称之为"出队"。所以，队列具有"先进先出"的特点。
    《图解Python》
    
    为了在多进程中应用队列这种数据结构，标准库模块multiprocessing中提供了三个类对象：
（1）Queue
（2）JoinableQueue
    它是Queue的子类，并添加了两个方法。
（3）SimpleQueue
    它是Queue的简化版。
    
    这三种队列都是多进程安全的，都实现了所有需要的同步机制。
"""

"""
    Queue的常见方法如下：
（1）__init__(self, maxsize=-1)
    队列中所能容纳的对象数量可以在创建Queue实例对象时进行指定；如果不指定，默认没有数量限制。
（2）qsize(self)
    返回队列中的消息数量。
（3）empty(self)
    如果队列为空，返回True，反之返回False。
（4）full(self)
    如果队列已满，返回True，反之返回False。
（5）put(self, obj, block=True, timeout=None)
    将参数obj指定的对象入队。
    当参数block的值为False时，如果队列已满导致无法入队，则会抛出异常；
    当参数block的值为True并且没有设置参数timeout的值时，如果队列已满导致无法入队，则程序会被
阻塞，直到队列中腾出位置再入队。
    当参数block的值为True并且设置了参数timeout的值时，如果队列已满导致无法入队，则程序会被
阻塞，若timeout秒之内队列中腾出位置则入队，若timeout秒之后队列仍是满的则抛出异常。
（6）get(self, block=True, timeout=None)
    将队头的对象出队。
    当参数block的值为False时，如果队列为空导致无法出队，则会抛出异常；
    当参数block的值为True并且没有设置参数timeout的值时，如果队列为空导致无法出队，则程序会被
阻塞，直到队列不再为空时再出队。
    当参数block的值为True并且设置了参数timeout的值时，如果队列为空导致无法出队，则程序会被
阻塞，若timeout秒之内队列中不再为空时再出队，若timeout秒之后队列仍为空则抛出异常。
（7）put_nowait(obj)
    等同于put(obj, False)。
（8）get_nowait()
    等同于get(False)。
"""
from multiprocessing import Queue

q = Queue()

print(q.empty())    # True


q.put('obj1')
q.put('obj2')

print(q.full())     # False

q.put('obj3')

print(q.full())     # True


print(q.get())      # obj1
print(q.get())      # obj2

print(q.empty())    # False

print(q.get())      # obj3

print(q.empty())    # True
