from threading import Thread, Event, current_thread
import time

event = Event()
# 用于判断 event 对象管理的内部标志是否被设置为 True
print(event.is_set())  # 刚开始是 False


def do_sth():
    print('%s开始等待' % current_thread().getName())
    # 当 event 对象管理的内部标志为 False 时调用 wait() 方法
    # 会将调用方法的线程阻塞
    event.wait()
    print('%s结束等待' % current_thread().getName())


for i in range(3):
    Thread(target=do_sth).start()

time.sleep(2)

event.set()

"""
False
Thread-1开始等待
Thread-2开始等待
Thread-3开始等待
Thread-1结束等待
Thread-2结束等待
Thread-3结束等待
"""

"""
小结

标准库模块 threading 中提供了一个类对象 Event，也可以实现多线程间的同步。
Event 实例对象管理着一个内部标志。
通过改变这个内部标志的值，可以让一个线程给其它处于阻塞状态的线程发送一个事件信号。
从而唤醒这些线程，让它们转为运行状态。

Event 的方法：
set() 方法：用于将内部标志设置为 True。
is_set() 方法：用于判断内部标志是否被设置为 True。
clear() 方法：将内部标志设置为 False，与 set() 方法对应。
wait() 方法：当内部标志位 False 时，调用该方法的线程会被阻塞。
             直到另外一个线程调用了方法 set() 将内部标志设置为 True，
             被阻塞的线程才会转为运行状态。
"""
