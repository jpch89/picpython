from multiprocessing import current_process, Process
import time


class MyProcess(Process):
    def run(self):
        print('子进程%d启动' % current_process().pid)
        time.sleep(2)
        print('子进程%d结束' % current_process().pid)


if __name__ == '__main__':
    print('父进程%d启动' % current_process().pid)
    mp = MyProcess()
    mp.daemon = True
    mp.start()
    time.sleep(1)
    print('父进程%d结束' % current_process().pid)

# 不设置守护线程
"""
父进程1496启动
父进程1496结束
子进程7208启动
子进程7208结束
"""

# 设置守护线程
"""
父进程928启动
子进程10868启动
父进程928结束
"""

"""
小结

可以在调用进程实例的 start() 方法之前将属性 daemon 设置为 True，
从而将进程设置为守护进程。
守护进程是为了守护父进程而存在的子进程。
当父进程结束时，守护进程就没有存在的意义了。
因此守护进程会随着父进程的结束而立刻结束。
"""
