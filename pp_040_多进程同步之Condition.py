from multiprocessing import Process, Condition
import time


class MyProcess1(Process):
    def __init__(self, name, cond):
        super().__init__(name=name)
        self.cond = cond

    def run(self):
        self.cond.acquire()
        print('%s说：1' % self.name)
        self.cond.notify()
        self.cond.wait()

        # 思考 2 秒之后再说
        time.sleep(2)
        print('%s说：11' % self.name)
        self.cond.notify()
        self.cond.wait()

        # 思考 2 秒之后再说
        time.sleep(2)
        print('%s说：111' % self.name)
        self.cond.notify()

        self.cond.release()


class MyProcess2(Process):
    def __init__(self, name, cond):
        super().__init__(name=name)
        self.cond = cond

    def run(self):
        time.sleep(1)
        self.cond.acquire()

        # 思考 2 秒之后再说
        time.sleep(2)
        print('%s说：2' % self.name)
        self.cond.notify()
        self.cond.wait()

        # 思考 2 秒之后再说
        time.sleep(2)
        print('%s说：22' % self.name)
        self.cond.notify()
        self.cond.wait()

        # 思考 2 秒之后再说
        time.sleep(2)
        print('%s说：222' % self.name)

        self.cond.release()

if __name__ == '__main__':
    cond = Condition()
    MyProcess1('Process1', cond).start()
    MyProcess2('Process2', cond).start()

"""
Process1说：1
Process2说：2
Process1说：11
Process2说：22
Process1说：111
Process2说：222
"""
