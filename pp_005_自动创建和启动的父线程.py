import time, threading

# 方法 current_thread() 用于获得当线程实例
# 即自动创建并启动的父线程
print('自动创建并启动了父（主）线程：%s'
    % threading.current_thread().getName())
time.sleep(20)
"""
自动创建并启动了父（主）线程：MainThread
"""

"""
小结

任何进程（不管是自动还是主动创建的进程）都会自动创建并启动一个线程。
该线程被称作父（主）线程。
父（主）线程的默认名称是 MainThread。
"""
