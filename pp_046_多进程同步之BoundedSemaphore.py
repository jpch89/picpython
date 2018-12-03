from multiprocessing import BoundedSemaphore

if __name__ == '__main__':
    bsem = BoundedSemaphore(3)

    bsem.acquire()
    bsem.release()
    bsem.release()  # 在 Mac OS 平台上不会抛出异常

"""
Traceback (most recent call last):
  File "D:/code/picpython/pp_046_多进程同步之BoundedSemaphore.py", line 8, in <module>
    bsem.release()
ValueError: semaphore or lock released too many times
"""
