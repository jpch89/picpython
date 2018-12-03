"""
from threading import Lock

lock = Lock()

lock.acquire()
print('获得锁')

lock.acquire()
print('获得锁')

lock.release()
print('释放锁')

lock.release()
print('释放锁')
"""

"""
获得锁
"""

"""
在同一线程中，当调用了 Lock 的方法 acquire() 之后，
如果在调用方法 release() 之前再次调用了方法 acquire()，也会导致死锁。

threading 模块还给我们提供了一个 RLock 类。
该类也提供了 acquire() 和 release() 方法。
RLock 是 reentrant lock 的缩写，意思是可重入锁。
与 Lock 不同的是，在同一个线程中，当调用了 RLock 的方法 acquire() 之后，
可以在调用方法 release() 之前，多次调用方法 acquire() 而不会导致死锁。
"""

from threading import RLock

lock = RLock()

lock.acquire()
print('获得锁')

lock.acquire()
print('获得锁')

lock.release()
print('释放锁')

lock.release()
print('释放锁')

"""
获得锁
获得锁
释放锁
释放锁
"""
