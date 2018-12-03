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
    # with ProcessPoolExecutor(max_workers=3) as ppe:
    # 我这么写：
    with ProcessPoolExecutor(3) as ppe:
        # for i in range(1, 7):
        #     ppe.submit(do_sth, i)
        # 不用调用 shutdown
        # 离开上下文的时候会自动调用 wait 参数为 True 的 shutdown 方法

        # for ... in ... 循环也可以这么写
        # 这个 map 类似内置函数 map
        ppe.map(do_sth, range(1, 7))

    print('父进程结束')
"""
父进程启动
子进程1启动
子进程2启动
子进程3启动
子进程1结束，耗时0.48秒
子进程4启动
子进程2结束，耗时1.08秒
子进程5启动
子进程3结束，耗时1.33秒
子进程6启动
子进程4结束，耗时0.96秒
子进程5结束，耗时1.80秒
子进程6结束，耗时1.89秒
父进程结束
"""

"""
小结

类对象 ProcessPoolExecutor 遵守上下文管理协议，
所以可以使用 with 语句。
在离开运行时上下文时，会自动调用 shutdown 方法，默认 wait=True。
"""
