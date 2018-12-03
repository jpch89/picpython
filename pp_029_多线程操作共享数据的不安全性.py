from threading import Thread

num = 0


def do_sth():
    global num
    for i in range(1000000):
        # 相当于 num = num + 1
        # 首先计算 num + 1，存入临时变量
        # 然后将临时变量的值赋值给 num
        num += 1


t1 = Thread(target=do_sth)
t2 = Thread(target=do_sth)

t1.start()
t2.start()

# 父线程会等待两个子线程都执行完毕之后
# 再继续执行
t1.join()
t2.join()

print(num)  # 预期为 2000000 两百万
"""
1458111
"""