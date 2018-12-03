from multiprocessing import Pipe

conn1, conn2 = Pipe()

conn1.send('conn1 第 1 次发送的数据')
conn1.send('conn1 第 2 次发送的数据')

conn2.send('conn2 第 1 次发送的数据')
conn2.send('conn2 第 2 次发送的数据')

print(conn1.recv())
print(conn1.recv())

print(conn2.recv())
print(conn2.recv())

"""
conn2 第 1 次发送的数据
conn2 第 2 次发送的数据
conn1 第 1 次发送的数据
conn1 第 2 次发送的数据
"""

# 半双工
# c1 只能接收，c2 只能发送
c1, c2 = Pipe(False)

c2.send('c2发送的数据')
print(c1.recv())
"""
c2发送的数据
"""

# 如果让 c1 发送
# c1.send('c1发送的数据')
"""
OSError: connection is read-only
"""

# 如果让 c2 接收
# print(c2.recv())
"""
OSError: connection is write-only
"""
