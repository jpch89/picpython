"""
小结
标准库模块 concurrent.futures 提供了一个类对象 ThreadPoolExecutor，
用于表示线程池。
与 threading.ThreadPool 相比，ThreadPoolExecutor 的功能和性能更加强大。

类对象 ThreadPoolExecutor 遵守了上下文管理协议，
所以可以使用 with 语句。
这样，在离开运行时上下文时会自动调用方法 shutdown(wait=True)。
"""

from concurrent.futures import ThreadPoolExecutor
import time, random

print('父线程启动')


def do_sth(i):
    print('子线程%d启动' % i)
    start = time.time()
    time.sleep(random.random() * 2)
    end = time.time()
    print('子线程%d结束，耗时%.2f秒' % (i, end - start))


"""
# 将线程池所能容纳的最大线程指定为3
tpe = ThreadPoolExecutor(max_workers=3)

# 将需要线程池处理的任务全部交给线程池
# 此后会创建并启动由线程池管理的子线程
for i in range(1, 11):
    tpe.submit(do_sth, i)

# 父线程被阻塞
# 线程池管理的所有子线程执行完成之后，父线程再从被阻塞的地方继续执行
tpe.shutdown(wait=True)
"""

with ThreadPoolExecutor(max_workers=3) as tpe:
    """
    for i in range(1, 11):
        tpe.submit(do_sth, i) 
    """
    tpe.map(do_sth, range(1, 11))

print('父线程结束')

"""
父线程启动
子线程1启动
子线程2启动
子线程3启动
子线程3结束，耗时0.98秒
子线程4启动
子线程2结束，耗时1.09秒
子线程5启动
子线程1结束，耗时1.75秒
子线程6启动
子线程4结束，耗时1.95秒
子线程7启动
子线程6结束，耗时1.19秒
子线程8启动
子线程5结束，耗时1.92秒
子线程9启动
子线程9结束，耗时0.35秒
子线程10启动
子线程7结束，耗时0.60秒
子线程8结束，耗时1.46秒
子线程10结束，耗时1.09秒
父线程结束
"""
