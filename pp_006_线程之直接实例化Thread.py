from threading import Thread, current_thread
import time

print('父线程【%s】启动' % (current_thread().getName()))


def do_sth(arg1, arg2):
    print('子线程【%s】启动' % current_thread().getName())
    time.sleep(20)
    print('arg1 = %d, arg2 = %d' % (arg1, arg2))
    print('子线程【%s】结束' % current_thread().getName())


# thread = Thread(target=do_sth, args=(5, 8), name='我的线程')
thread = Thread(target=do_sth, args=(5, 8))
thread.start()

time.sleep(25)
print('父线程【%s】结束' % current_thread().getName())

"""
父线程【MainThread】启动
子线程【Thread-1】启动
arg1 = 5, arg2 = 8
子线程【Thread-1】结束
父线程【MainThread】结束
"""

"""
小结

标准库模块 threading 中提供了一个类 Thread，用于表示线程。

使用 Thread 类创建并启动子线程的第 1 种方式为：
1. 根据 Thread 类创建线程实例
2. 调用线程实例的 start() 方法启动线程。
   调用 start() 方法后，会自动调用方法 run()
   方法 run() 会自动调用参数 target 指定的函数

Thread 初始化方法 __init__() 的定义如下：
__init__(self, group=None, target=None, name=None, args=(), kwargs=None, daemon=None)
调用 __init__() 方法的时候必须指定关键字实参。
1. 参数 group 用于指定线程实例所属的线程组，默认不属于任何线程组；
2. 参数 target 用于指定被 run() 方法调用的函数，默认没有函数被调用；
3. 参数 name 用于指定创建的进程实例的名称，第 n 个子线程的默认名称为 Thread-n；
4. 参数 args 用于指定 target 接收的位置参数，用元组表示，默认不接收位置参数；
5. 参数 kwargs 用于指定 target 接收的关键字参数，用字典表示，默认不接收关键字参数；
6. 参数 daemon 用于指定线程实例是否是守护线程，默认不是守护线程。
"""
