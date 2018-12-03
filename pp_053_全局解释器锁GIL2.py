from threading import Thread

def do_sth():
    while True:
        pass


Thread(target=do_sth).start()
Thread(target=do_sth).start()

do_sth()
"""
三个线程并没有占满 8 核 CPU 中的其中三核，而只占满了其中一核。
因此，多线程并不能实现并行（不能同时处理多个任务），
而只能实现并发（交替处理多个任务）。
"""

"""
小结

我们编写的 Python 代码是通过 Python 解释器来执行的。
通常使用的 Python 解释器是官方提供的 CPython。
CPython 中有一个 GIL（Global Interpreter Lock，全局解释器锁）。
作用相当于 Lock，任何线程在执行前必须先获得 GIL。
一个线程在获得 GIL 后其他线程就不能执行，直到线程释放 GIL。
因此 GIL 保证了同一时刻只有一个线程可以执行，从而导致了 Python 中的多线程不能实现并行。
对于 
"""
