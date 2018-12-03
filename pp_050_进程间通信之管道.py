import random
import time
from multiprocessing import Process, Pipe
import os


# 发送数据的子进程执行的代码
# 参数是管道的发送端的连接
def send_data(conn):
    print('发送数据的子进程%d启动' % os.getpid())

    for obj in range(1, 10):
        print('发送数据：%s' % obj)
        conn.send(obj)
        time.sleep(random.random() * 2)

    print('发送数据：None')
    conn.send(None)

    print('发送数据的子进程%d结束' % os.getpid())


# 接收数据的子进程执行的代码
# 参数是管道的接收端的连接
def recv_data(conn):
    print('接收数据的子进程%d启动' % os.getpid())

    while True:
        item = conn.recv()
        if item is None:
            print('接收数据：None')
            break
        print('接收数据：%s' % item)

        time.sleep(random.random() * 2)
    print('接收数据的子进程%d结束' % os.getpid())


if __name__ == '__main__':
    print('父进程%d启动' % os.getpid())

    cr, cs = Pipe(False)
    ps = Process(target=send_data, args=(cs, ))
    pr = Process(target=recv_data, args=(cr, ))

    ps.start()
    pr.start()

    ps.join()
    pr.join()

    print('父进程%d结束' % os.getpid())

"""
父进程52756启动
发送数据的子进程50836启动
发送数据：1
接收数据的子进程50388启动
接收数据：1
发送数据：2
接收数据：2
发送数据：3
接收数据：3
发送数据：4
接收数据：4
发送数据：5
接收数据：5
发送数据：6
接收数据：6
发送数据：7
发送数据：8
接收数据：7
发送数据：9
接收数据：8
发送数据：None
发送数据的子进程50836结束
接收数据：9
接收数据：None
接收数据的子进程50388结束
父进程52756结束
"""

"""
小结

如果想要实现进程之间的通信，管道也是常见的实现方式之一。
"""