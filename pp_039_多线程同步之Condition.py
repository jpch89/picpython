from threading import Thread, Condition
import time

cond = Condition()


class MyThread1(Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        cond.acquire()
        print('%s说：1' % self.name)
        cond.notify()
        cond.wait()

        # 思考 2 秒之后再说
        time.sleep(2)
        print('%s说：11' % self.name)
        cond.notify()
        cond.wait()

        # 思考 2 秒之后再说
        time.sleep(2)
        print('%s说：111' % self.name)
        cond.notify()

        cond.release()


class MyThread2(Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        time.sleep(1)
        cond.acquire()

        # 思考 2 秒之后再说
        time.sleep(2)
        print('%s说：2' % self.name)
        cond.notify()
        cond.wait()

        # 思考 2 秒之后再说
        time.sleep(2)
        print('%s说：22' % self.name)
        cond.notify()
        cond.wait()

        # 思考 2 秒之后再说
        time.sleep(2)
        print('%s说：222' % self.name)

        cond.release()


MyThread1('Thread1').start()

MyThread2('Thread2').start()
"""
Thread1说：1
Thread2说：2
Thread1说：11
Thread2说：22
Thread1说：111
Thread2说：222
"""
