"""
def do_sth():
    while True:
        pass


do_sth()
"""

"""
单进程或者单线程占满了 8 核 CPU 中的其中一核。
"""

from multiprocessing import Process


def do_sth():
    while True:
        pass


if __name__ == '__main__':
    Process(target=do_sth).start()
    Process(target=do_sth).start()
    do_sth()
"""
三个进程占满了 8 核 CPU 的其中三核。
因此，多进程可以实现并行（真正的同时处理多个任务），
从而发挥多核 CPU 的最大性能。
"""
