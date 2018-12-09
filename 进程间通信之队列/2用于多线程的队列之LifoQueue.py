
"""用于多线程的队列之LifoQueue"""

"""
    LifoQueue的特点是Lifo（Last in first out，后进先出），也就是说，入队和出队都是在队尾。
    后进先出的队列其实就是栈。
    《图解Python》
"""
from queue import LifoQueue

lq = LifoQueue()

lq.put('obj1')
lq.put('obj2')
lq.put('obj3')

print(lq.get())     # obj3
print(lq.get())     # obj2
print(lq.get())     # obj1