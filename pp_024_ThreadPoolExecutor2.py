from concurrent.futures import ThreadPoolExecutor
import time


def do_sth(i):
    time.sleep(2)
    return i * i


# 让多进程异步执行
if __name__ == '__main__':
    objs = []
    with ThreadPoolExecutor(3) as tpe:
        for i in range(1, 5):
            future = tpe.submit(do_sth, i)
            # 异步，无需等待 do_sth 执行完毕
            print(future)
            objs.append(future)

    for obj in objs:
        print(obj.result())

"""
<Future at 0x261eaddea90 state=running>
<Future at 0x261eb329ef0 state=running>
<Future at 0x261eb33f208 state=running>
<Future at 0x261eb33fa90 state=pending>
1
4
9
16
"""
