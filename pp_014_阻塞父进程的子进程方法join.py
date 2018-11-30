from multiprocessing import Process, current_process
import time


class MyProcess(Process):
    def run(self):
        print('子进程%d启动' % current_process().pid)
        time.sleep(2)
        print('子进程%d结束' % current_process().pid)


if __name__ == "__main__":
    print('父进程%d启动' % current_process().pid)
    mp = MyProcess()
    mp.start()
    # time.sleep(5)
    # mp.join()
    mp.join(1)  # 阻塞一秒之后，父进程脱离阻塞状态
    print('父进程%d结束' % current_process().pid)

"""
# 没有加入 mp.join()
父进程1564启动
父进程1564结束
子进程1108启动
子进程1108结束

# 加入 mp.join() 之后
父进程12284启动
子进程14028启动
子进程14028结束
父进程12284结束

# 使用 mp.join(1) 之后
父进程14512启动
子进程15140启动
父进程14512结束
子进程15140结束
"""

"""
小结

在父进程中创建并启动子进程后，可以调用子进程的方法 join()。
这样，子进程会把父进程阻塞，父进程会等子进程执行完之后再从被阻塞的地方继续执行。
在调用方法 join() 时，可以指定参数 timeout，从而指定子进程阻塞父进程的时间。
"""