from threading import Thread, current_thread
import time

print('父线程【%s】启动' % current_thread().getName())


class MyThread(Thread):
    def __init__(self, name, args):
        super().__init__(name=name)
        self.args = args

    def run(self):
        print('子线程【%s】启动' % current_thread().getName())
        time.sleep(20)
        print('arg1 = %d, arg2 = %d' % self.args)
        print('子线程【%s】结束' % current_thread().getName())


mt = MyThread(name='我的线程', args=(5, 8))
mt.start()

time.sleep(25)

print('父线程【%s】结束' % current_thread().getName())
"""
父线程【MainThread】启动
子线程【我的线程】启动
arg1 = 5, arg2 = 8
子线程【我的线程】结束
父线程【MainThread】结束
"""

"""
使用 Thread 类创建并启动子线程的第 2 种方式为：
1. 自定义继承自 Thread 的类，重写特殊方法 __init__() 和 run() 方法；
2. 根据自定义的类对象创建线程实例；
3. 调用线程实例的 start() 方法启动线程。
   调用 start() 方法后，会自动调用重写后的 run() 方法。

与第 1 种方式相比，相当于把参数 target 指定的函数的函数体转移到了 run() 方法中。
因此在创建线程实例时，无需再指定参数 target。
第 1 种创建线程实例时指定的其他参数，在第 2 种方式中可以传递给重写后的特殊方法 __init__()。

"""
