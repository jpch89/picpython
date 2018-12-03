from concurrent.futures import ProcessPoolExecutor
import time


def do_sth(i):
    time.sleep(2)
    return i * i

"""
if __name__ == '__main__':
    with ProcessPoolExecutor(3) as ppe:
        for i in range(1, 5):
            future = ppe.submit(do_sth, i)
            # 同步，需要等待 do_sth() 执行完毕
            print(future.result())
"""
"""
1
4
9
16
"""

# 让多进程异步执行
if __name__ == '__main__':
    objs = []
    with ProcessPoolExecutor(3) as ppe:
        for i in range(1, 5):
            future = ppe.submit(do_sth, i)
            # 异步，无需等待 do_sth 执行完毕
            print(future)
            objs.append(future)

    for obj in objs:
        print(obj.result())
"""
<Future at 0x1c3568c94a8 state=running>
<Future at 0x1c356903a58 state=running>
<Future at 0x1c356903fd0 state=pending>
<Future at 0x1c3569190f0 state=pending>
1
4
9
16
"""

"""
小结

方法 submit() 的返回值是一个 Future 实例，
表示子进程所调用的那个函数的执行。
可以调用 Future 的方法 result() 来得到函数的返回值。
result() 是一个同步方法，直到 do_sth() 执行完毕之后 result() 才会返回。
同步就意味着等待和阻塞，也就是每个子进程需要依次执行。
"""
