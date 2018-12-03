from threading import Timer
import time


def do_sth():
    print('Hello Timer!')
    global timer
    timer = Timer(1, do_sth)
    timer.start()


timer = Timer(2, do_sth)
timer.start()

time.sleep(5)

timer.cancel()

"""
Hello Timer!
Hello Timer!
Hello Timer!
"""

"""
小结

定时器只执行一次。
如果需要每隔一段时间执行一次，则需要在子线程调用的函数内部再次创建与启动定时器线程。
"""
