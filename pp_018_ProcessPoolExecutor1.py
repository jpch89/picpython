from concurrent.futures import ProcessPoolExecutor
import time, random


def do_sth(i):
    start = time.time()
    print('子进程%d启动' % i)
    time.sleep(random.random() * 2)
    end = time.time()
    print('子进程%d结束，耗时%.2f秒' % (i, end - start))


if __name__ == '__main__':
    print('父进程启动')
    # 将进程池所能容纳的最大进程数指定为 3
    # ppe = ProcessPoolExecutor(max_workers=3)
    # 我这么写：
    ppe = ProcessPoolExecutor(3)

    for i in range(1, 7):
        # 将需要进程池处理的任务全部交给进程池
        # 此后会创建并启动由进程池所管理的子进程
        ppe.submit(do_sth, i)

    # 关闭进程池，并阻塞父进程
    # 相当于合并了 Pool 类的 close() 和 join() 方法
    # ppe.shutdown(wait=True)
    # 其实函数定义中，默认 wait=True
    # 我这么写：
    ppe.shutdown()
    print('父进程结束')

"""
父进程启动
子进程1启动
子进程2启动
子进程3启动
子进程3结束，耗时0.76秒
子进程4启动
子进程2结束，耗时1.45秒
子进程5启动
子进程5结束，耗时0.07秒
子进程6启动
子进程4结束，耗时0.82秒
子进程1结束，耗时1.98秒
子进程6结束，耗时1.30秒
父进程结束
"""

"""
小结

标准库模块 concurrent.futures 中提供了一个类对象 ProcessPoolExecutor，
也用于表示进程池。
与 multiprocessing 中的 Pool 相比，ProcessPoolExecutor 的功能和性能更加强大。
"""
