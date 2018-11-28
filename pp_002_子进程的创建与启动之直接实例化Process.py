from multiprocessing import Process, current_process
import time

"""
使用 multiprocessing.Process 实例化的进程必须加 if __name___ == '__main__'。
否则会报错。

RuntimeError:
        An attempt has been made to start a new process before the
        current process has finished its bootstrapping phase.

        This probably means that you are not using fork to start your
        child processes and you have forgotten to use the proper idiom
        in the main module:

            if __name__ == '__main__':
                freeze_support()
                ...

        The "freeze_support()" line can be omitted if the program
        is not going to be frozen to produce an executable.
"""


def do_sth(arg1, arg2):
    print('子进程启动(%d--%s)' % (
        current_process().pid, current_process().name))
    print('arg1 = %d, arg2 = %d' % (arg1, arg2))
    print('子进程结束(%d--%s)' % (
        current_process().pid, current_process().name))


if __name__ == '__main__':
    print('父进程启动(%d--%s)' % (
    current_process().pid, current_process().name))
    process = Process(target=do_sth, args=(5, 8))
    process.start()
    time.sleep(2)
    print('父进程结束(%d--%s)' % (
    current_process().pid, current_process().name))

"""
父进程启动(19320--MainProcess)
子进程启动(17084--Process-1)
arg1 = 5, arg2 = 8
子进程结束(17084--Process-1)
父进程结束(19320--MainProcess)
"""

"""
小结

标准库模块 multiprocessing 中提供了一个类 Process，用于表示进程。
使用类 Process 创建并启动子进程的第 1 种方式：
1. 根据类 Process 创建进程实例；
2. 调用进程实例的方法 start() 启动进程：
   自动调用 run() 方法；
   run() 方法自动调用通过 target 参数指定的函数。

Process 的特殊方法 __init__() 的定义如下：
__init__(self, group=None, target=None, name=None, args=(), kwargs={})

调用 __init__() 时必须指定关键字实参，其中：
1. 参数 group 用于指定进程实例所属的进程组，默认不属于任何进程组；
2. 参数 target 用于指定被方法 run() 调用的函数，默认没有函数被调用；
3. 参数 name 用于指定创建的进程实例的名称，第 n 个子进程的默认名称为 Process-n；
4. 参数 args 用于指定 target 接收的位置参数，用元组表示，默认不接收位置参数；
5. 参数 kwargs 用于指定 target 接收的关键字参数，用字典表示，默认不接收关键字参数。
"""
