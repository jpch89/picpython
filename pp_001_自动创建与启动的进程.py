import os, time

# 打印当前进程的 id
# getpid：get process id
print(os.getpid())
# 打印当前进程父进程的 id
# getppid：get parent process id
print(os.getppid())
"""
18512
14872
"""

print('-' * 20)

import multiprocessing
# 获取当前进程的实例对象（自动创建并启动的进程）
print(multiprocessing.current_process())
print(multiprocessing.current_process().pid)
"""
--------------------
<_MainProcess(MainProcess, started)>
18512
"""

# 让 py 文件至少运行 20 秒钟
time.sleep(20)

"""
当在 PyCharm / Sublime Text 中运行一个 py 文件时，
PyCharm 或 Sublime Text 对应的进程会自动创建并启动一个新进程，
其默认名称为 Python。
当 py 文件运行结束时，自动创建并启动的新进程也随之结束。

创建并启动子进程的进程被称为父进程。
"""
