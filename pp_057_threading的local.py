from threading import local, current_thread, Thread

# local 是类对象，local() 创建类对象的实例对象
thread_local = local()


def do_sth(arg1, arg2, arg3):
    thread_local.local_var1 = arg1
    thread_local.local_var2 = arg2
    thread_local.local_var3 = arg3

    fun1()
    fun2()
    fun3()


def fun1():
    print('%s: %s -- %s -- %s' % (current_thread().name,
                                  thread_local.local_var1,
                                  thread_local.local_var2,
                                  thread_local.local_var3))


def fun2():
    print('%s: %s -- %s -- %s' % (current_thread().name,
                                  thread_local.local_var1,
                                  thread_local.local_var2,
                                  thread_local.local_var3))


def fun3():
    print('%s: %s -- %s -- %s' % (current_thread().name,
                                  thread_local.local_var1,
                                  thread_local.local_var2,
                                  thread_local.local_var3))


t1 = Thread(target=do_sth, args=('a', 'b', 'c'))
t2 = Thread(target=do_sth, args=('d', 'e', 'f'))

t1.start()
t2.start()

"""
Thread-1: a -- b -- c
Thread-1: a -- b -- c
Thread-1: a -- b -- c
Thread-2: d -- e -- f
Thread-2: d -- e -- f
Thread-2: d -- e -- f
"""

"""
应用场景

为每一个线程都绑定一个 HTTP 请求或者数据库的连接。
线程内所有函数都可以访问这些变量。
"""
