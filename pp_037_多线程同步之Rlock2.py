from threading import RLock, Thread

numa = 0
numb = 0

rlock = RLock()


def do_sth():
    rlock.acquire()
    try:
        adda()
        addb()
    finally:
        rlock.release()


def adda():
    global numa
    rlock.acquire()
    try:
        numa += 1
    finally:
        rlock.release()


def addb():
    global numb
    with rlock:
        numb += 1


tlist = []
for i in range(10):
    t = Thread(target=do_sth)
    tlist.append(t)
    t.start()

for item in tlist:
    item.join()

print(numa)
print(numb)

"""
10
10
"""

"""
小结

RLock 也遵守上下文管理协议，所以可以使用 with 语句。
"""