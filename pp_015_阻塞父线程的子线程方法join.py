

"""
小结

在父线程中创建并启动子线程后，可以调用子线程的方法 join()。
这样，子线程会把父线程阻塞。
父线程会等子线程执行完成之后再从被阻塞的地方继续执行。
在调用方法 join() 时，可以指定参数 timeout，从而指定子进程阻塞父进程的时间。
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
mt.start()
mt.join(1)

print('父线程【%s】结束' % current_thread().getName())
"""
加入 mt.join() 之前
父线程【MainThread】启动
子线程【Thread-1】启动
父线程【MainThread】结束
子线程【Thread-1】结束

加入 mt.join() 之后
父线程【MainThread】启动
子线程【Thread-1】启动
子线程【Thread-1】结束
父线程【MainThread】结束

也可以指定阻塞时间为 1 秒：mt.join(1)
父线程【MainThread】启动
子线程【Thread-1】启动
父线程【MainThread】结束
子线程【Thread-1】结束
"""
