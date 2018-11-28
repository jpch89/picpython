from multiprocessing import current_process, Process
import time

class MyProcess(Process):
    def __init__(self, name, args):
        super().__init__(name=name)
        self.args = args

    def run(self):
        print('子进程启动(%d--%s)' % (
            current_process().pid, current_process().name))
        print('arg1 = %d, arg2 = %d' % self.args)
        print('子进程结束(%d--%s)' % (
            current_process().pid, current_process().name))

if __name__ == '__main__':
    print('父进程启动(%d--%s)' % (
        current_process().pid, current_process().name))
    mp = MyProcess('我的进程', args=(5, 8))
    mp.start()
    time.sleep(2)
    print('父进程结束(%d--%s)' % (
        current_process().pid, current_process().name))

"""
父进程启动(18588--MainProcess)
子进程启动(15804--我的进程)
arg1 = 5, arg2 = 8
子进程结束(15804--我的进程)
父进程结束(18588--MainProcess)
"""

"""
小结

使用 Process 类创建并启动子进程的第 2 种方式为：
1. 自定义一个类，继承自 Process，重写 __init__() 和 run() 方法；
2. 根据自定义类创建进程实例；
3. 调用进程实例的 start() 方法，启动进程。
   调用 start() 之后，会自动调用重写后的 run() 方法。

与第 1 种方式相比，相当于把参数 target 指定的函数的函数体转移到了方法 run() 中。
因此，在创建进程实例时无需再指定参数 target。

第 1 种方式创建进程实例时指定的其它参数，在第 2 种方式中可以传递给重写后的特殊方法 __init__()。
"""
