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
    mp.join()
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
"""

