from threading import BoundedSemaphore, Semaphore

sem = Semaphore(3)
sem.acquire()
sem.release()
sem.release()
"""
不会报错！
"""

bsem = BoundedSemaphore(3)

bsem.acquire()
bsem.release()
bsem.release()

"""
ValueError: Semaphore released too many times
"""

"""
小结

如果我们调用方法 release 的次数，比调用 acquire 的次数多，
计数器的当前值就会超过它的初始值。
为了确保能够及时检测到程序中的这种 Bug，可以使用 BoundedSemaphore 来替代 Semaphore。
一旦程序中出现这种 Bug，就会抛出异常 ValueError。
"""
