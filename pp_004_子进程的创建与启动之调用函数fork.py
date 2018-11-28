import os

try:
    pid = os.fork()
except AttributeError:
    print('你的操作系统不支持调用函数 fork()')
    exit()

if pid < 0:
    print('复制子进程失败')
elif pid == 0:
    print('我是子进程%d，我的父进程是%d' % (
        os.getpid(), os.getppid()))
else:
    print('我是父进程%d，我的子进程是%d' % (
        os.getpid(), pid))

"""
Win 系统报错：
AttributeError: module 'os' has no attribute 'fork'
"""

"""
小结

标准库模块 os 中提供了一个函数 fork()，用于将当前进程复制一份子进程。
而后父进程和子进程从调用 fork() 处开始分叉（fork 的含义）。
兵分两路，继续并行运行后面的程序。
与普通函数不同的是，函数 fork() 会返回两次，分别在父进程和子进程内返回。
返回值有三种情况：
1. 返回值小于 0，表示复制子进程失败；
2. 返回值为 0，表示处在子进程中；
3. 返回值大于 0，表示处在父进程中，返回值就是子进程的 id。
在 Windows 操作系统上无法调用 fork() 函数，因为 fork() 函数不是跨平台的。
而模块 multiprocessing 是跨平台的
"""
