from multiprocessing import Process, Event, current_process
import time




def do_sth(event):
    print('%d开始等待' % current_process().pid)
    # 当 event 对象管理的内部标志为 False 时调用 wait() 方法
    # 会将调用方法的进程阻塞
    event.wait()
    print('%d结束等待' % current_process().pid)

if __name__ == '__main__':
    event = Event()
    # 用于判断 event 对象管理的内部标志是否被设置为 True
    print(event.is_set())  # 刚开始是 False
    for i in range(3):
        Process(target=do_sth, args=(event, )).start()
    time.sleep(2)
    event.set()

"""
False
51660开始等待
48088开始等待
52972开始等待
48088结束等待
51660结束等待
52972结束等待
"""

"""
小结

标准库模块 multiprocessing 中提供了一个类对象 Event，也可以实现多进程间的同步。
Event 实例对象管理着一个内部标志。
通过改变这个内部标志的值，可以让一个进程给其它处于阻塞状态的进程发送一个事件信号。
从而唤醒这些进程，让它们转为运行状态。

Event 的方法：
set() 方法：用于将内部标志设置为 True。
is_set() 方法：用于判断内部标志是否被设置为 True。
clear() 方法：将内部标志设置为 False，与 set() 方法对应。
wait() 方法：当内部标志位 False 时，调用该方法的进程会被阻塞。
             直到另外一个进程调用了方法 set() 将内部标志设置为 True，
             被阻塞的进程才会转为运行状态。
"""
