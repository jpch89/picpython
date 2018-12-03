"""
经典生产者消费者问题：
假设有一群生产者（Producer）和一群消费者（Consumer）通过一个市场来交换产品。
生产者的策略是：如果市场上剩余的产品少于 20 个，那么就生产 4 个产品放到市场上；
消费者的策略是：如果市场上剩余的产品多余 10 个，那么就从市场上消费 3 个产品。
"""

from multiprocessing import Process, Condition, Value
import time


class Producer(Process):
    def __init__(self, cond, count, *args, **kwargs):
        super(Process, self).__init__(*args, **kwargs)
        self.cond = cond
        self.count = count

    def run(self):
        # global count, cond
        while True:
            self.cond.acquire()
            if self.count.value < 20:
                self.count.value += 4
                print('%s：生产者生产了 4 个，当前总共 %d 个' % (
                    self.name, self.count.value))
                self.cond.notify()
            else:
                print('%s：不生产，等待' % self.name)
                self.cond.wait()
            self.cond.release()
            time.sleep(2)


class Consumer(Process):
    def __init__(self, cond, count, *args, **kwargs):
        super(Process, self).__init__(*args, **kwargs)
        self.cond = cond
        self.count = count

    def run(self):
        # global count, cond


        while True:
            self.cond.acquire()
            if self.count.value > 10:
                self.count.value -= 3
                print('%s：消费者消费了 3 个，当前总共 %d 个' % (
                    self.name, self.count.value))
                self.cond.notify()
            else:
                print('%s：不消费，等待' % self.name)
                self.cond.wait()
            self.cond.release()
            time.sleep(2)


if __name__ == '__main__':
    count = Value('i', 0)
    cond = Condition()
    
    for i in range(3):
        Producer(cond, count).start()

    for i in range(3):
        Consumer(cond, count).start()
