from multiprocessing import Process, current_process
import time


def do_sth():
    for i in range(5):
        print('%s: %d' % (current_process().name, i))
        time.sleep(2)


if __name__ == '__main__':
    for i in range(3):
        Process(target=do_sth).start()
    do_sth()

"""
MainProcess: 0
Process-1: 0
Process-2: 0
Process-3: 0
MainProcess: 1
Process-1: 1
Process-3: 1
Process-2: 1
MainProcess: 2
Process-1: 2
Process-2: 2
Process-3: 2
MainProcess: 3
Process-1: 3
Process-2: 3
Process-3: 3
MainProcess: 4
Process-1: 4
Process-3: 4
Process-2: 4
"""

"""
小结

默认情况下，多个进程的执行顺序和时间都是不确定的。
完全取决于操作系统的调度。
"""
