from threading import Thread, current_thread
import time


def do_sth():
    for i in range(5):
        print('%s: %d' % (current_thread().getName(), i))
        time.sleep(2)


if __name__ == '__main__':
    for i in range(3):
        Thread(target=do_sth).start()
    do_sth()

"""
Thread-1: 0
Thread-2: 0
Thread-3: 0
MainThread: 0
MainThread: 1
Thread-2: 1
Thread-1: 1
Thread-3: 1
MainThread: 2
Thread-3: 2
Thread-1: 2
Thread-2: 2
MainThread: 3
Thread-3: 3
Thread-1: 3
Thread-2: 3
MainThread: 4
Thread-2: 4
Thread-1: 4
Thread-3: 4
"""

"""
小结

默认情况下，多个进程的执行顺序和时间都是不确定的。
完全取决于操作系统的调度。
"""
