from multiprocessing import Pool
import time, random


# Win 系统下这个方法不能放到 main 代码块中
def do_sth(i):
    start = time.time()
    print('子进程%d启动' % i)
    time.sleep(random.random() * 2)
    end = time.time()
    print('子进程%d结束，耗时%.2f秒' % (i, end - start))


if __name__ == '__main__':
    print('父进程启动')

    # 将进程池所能容纳的最大进程数指定为 3
    pp = Pool(3)  # process pool

    for i in range(1, 6):
        # pp.apply_async() 与 start() 方法类似
        # 不同的是，我们创建的是由进程池管理的子进程
        pp.apply_async(do_sth, args=(i,))  # do_sth 可以是位置参数

    # 调用方法 pp.join() 之前必须先调用方法 close()
    # 调用方法 close() 之后就不能让进程池再管理新的进程了
    pp.close()

    # 父进程被阻塞
    # 进程池管理的所有子进程都执行完之后，
    # 父进程再从被阻塞的地方继续执行。
    pp.join()

    print('父进程结束')

"""
父进程启动
子进程1启动
子进程2启动
子进程3启动
子进程3结束，耗时1.27秒
子进程4启动
子进程4结束，耗时0.13秒
子进程5启动
子进程1结束，耗时1.47秒
子进程2结束，耗时1.99秒
子进程5结束，耗时1.09秒
父进程结束
"""

"""
小结

如果并发的任务数过多，一次性创建并启动大量的进程会给计算机带来很大的压力。
那么就可以使用进程池对创建与启动的进程进行限制和管理。
进程池中所能容纳的进程数目是固定的。

标准库模块 multiprocessing 中提供了一个类对象 Pool，用于表示进程池。
进程池中所能容纳的进程数目可以在创建 Pool 实例对象时进行指定；
如果不指定，默认大小是 CPU 的核数。
"""