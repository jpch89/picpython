from threading import Timer


def do_sth():
    print('Hello Timer!')


timer = Timer(2, do_sth)
timer.start()

"""
Hello Timer!
"""

"""
小结
如果想要在指定的时间片段之后再启动子线程，可以使用标准库模块 threading 提供的类对象 Timer。
用于表示定时器线程。
Timer 是 Thread 的子类，也是通过调用方法 start() 来启动线程。

"""