"""
由于多进程的执行是不确定的，导致多进程操作共享数据的结果是不可预期的。
常被称为不安全的。
"""

from multiprocessing import Process, Value

num = Value('i', 0)

def do_sth(num):
    for i in range(10000):
        num.value += 1

if __name__ == '__main__':
    t1 = Process(target=do_sth, args=(num, ))
    t2 = Process(target=do_sth, args=(num, ))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(num.value)

"""
11649
"""
