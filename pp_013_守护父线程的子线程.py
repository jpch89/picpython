"""
小结

在创建线程实例时，可以将参数 daemon 指定为 True，
从而将创建的线程设置为守护线程。
此外，也可以在调用线程实例的 start() 方法之前将 deamon 属性设置为 True，
或者调用线程实例的 setDaemon(True) 方法，从而将线程设置为守护线程。
守护线程是为了守护父线程而存在的子线程。
当父线程结束时，守护线程就没有存在的意义了。
因此，守护线程会随着父线程的结束而立刻结束。
"""

from threading import current_thread, Thread
import time

print('父线程【%s】启动' % current_thread().getName())


class MyThread(Thread):
    def run(self):
        print('子线程【%s】启动' % current_thread().getName())
        time.sleep(2)
        print('子线程【%s】结束' % current_thread().getName())


mt = MyThread()
# 以下两种方式等价：
mt.daemon = True
mt.setDaemon(True)
mt.start()

time.sleep(1)

print('父线程【%s】结束' % current_thread().getName())

"""
父线程【MainThread】启动
子线程【Thread-1】启动
父线程【MainThread】结束
"""
