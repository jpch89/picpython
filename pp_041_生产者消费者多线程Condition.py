"""
经典生产者消费者问题：
假设有一群生产者（Producer）和一群消费者（Consumer）通过一个市场来交换产品。
生产者的策略是：如果市场上剩余的产品少于 20 个，那么就生产 4 个产品放到市场上；
消费者的策略是：如果市场上剩余的产品多余 10 个，那么就从市场上消费 3 个产品。
"""

from threading import Thread, Condition
import time

cond = Condition()
count = 0


class Producer(Thread):
    def run(self):
        global count
        while True:
            cond.acquire()
            if count < 20:
                count += 4
                print('%s：生产者生产了 4 个，当前总共 %d 个' % (
                    self.name, count))
                cond.notify()
            else:
                print('%s：不生产，等待' % self.name)
                cond.wait()
            cond.release()
            time.sleep(2)



class Consumer(Thread):
    def run(self):
        global count
        while True:
            cond.acquire()
            if count > 10:
                count -= 3
                print('%s：消费者消费了 3 个，当前总共 %d 个' % (
                    self.name, count))
                cond.notify()
            else:
                print('%s：不消费，等待' % self.name)
                cond.wait()
            cond.release()
            time.sleep(2)

for i in range(3):
    Producer().start()

for i in range(3):
    Consumer().start()

"""
Thread-1：生产者生产了 4 个，当前总共 4 个
Thread-2：生产者生产了 4 个，当前总共 8 个
Thread-3：生产者生产了 4 个，当前总共 12 个
Thread-4：消费者消费了 3 个，当前总共 9 个
Thread-5：不消费，等待
Thread-6：不消费，等待
Thread-4：不消费，等待
Thread-3：生产者生产了 4 个，当前总共 13 个
Thread-2：生产者生产了 4 个，当前总共 17 个
Thread-1：生产者生产了 4 个，当前总共 21 个
Thread-4：消费者消费了 3 个，当前总共 18 个
Thread-3：生产者生产了 4 个，当前总共 22 个
Thread-2：不生产，等待
Thread-5：消费者消费了 3 个，当前总共 19 个
Thread-1：生产者生产了 4 个，当前总共 23 个
Thread-6：消费者消费了 3 个，当前总共 20 个
"""
