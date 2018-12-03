from threadpool import ThreadPool, makeRequests
import time, random


print('父线程启动')

# args_list = []
# for i in range(1, 11):
#     args_list.append(i)
# 看我一句搞定
args_list = [i for i in range(1, 11)]

def do_sth(i):
    start = time.time()
    print('子线程%d启动' % i)
    time.sleep(random.random() * 2)
    end = time.time()
    print('子线程%d结束，耗时%.2f秒' % (i, end - start))


# 将线程池所能容纳的最大线程数指定为 3
tp = ThreadPool(3)  # thread pool

# 通过 makeRequests 可以创建线程池所要处理的任务
requests = makeRequests(do_sth, args_list)

# 将需要线程池处理的任务全部交给线程池
# 此后会创建并启动由线程池管理的子线程
for req in requests:
    tp.putRequest(req)

# 父线程被阻塞
# 线程池被管理的所有子线程执行完之后
# 父线程再从被阻塞的地方继续执行
tp.wait()

print('父线程结束')
"""
父线程启动
子线程1启动
子线程2启动
子线程3启动
子线程2结束，耗时0.12秒
子线程4启动
子线程3结束，耗时0.55秒
子线程5启动
子线程5结束，耗时0.35秒
子线程6启动
子线程4结束，耗时1.02秒
子线程7启动
子线程1结束，耗时1.63秒
子线程8启动
子线程6结束，耗时0.82秒
子线程9启动
子线程9结束，耗时0.10秒
子线程10启动
子线程7结束，耗时0.99秒
子线程8结束，耗时0.99秒
子线程10结束，耗时1.50秒
父线程结束
"""

"""
小结

如果并发的任务数过多，一次性创建并启动大量的线程会给计算机带来很大的压力。
那么就可以使用线程池对创建与启动的线程进行限制和管理。
线程池中所能容纳的线程数目是固定的。

第三方库 threadpool 中提供了一个类对象 ThreadPool，用于表示线程池。
线程池中所能容纳的线程数目可以在创建 ThreadPool 实例对象时进行指定；
如果不指定，默认大小是 CPU 的核数。
"""
