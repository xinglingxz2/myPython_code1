'''  Python教程 8-1-2
  Struct模块的对象:  接收数据(对外软件数据传输协议）
'''

from socket import *
import struct

s = socket(AF_INET,SOCK_DGRAM)  # 创建udp套接字
s.bind(('127.0.0.1',8888))

st = struct.Struct('i32sif')   # 规定数据格式  创建Struct模块的对象

f = open('student.txt','a')  # 打开文件

while True:
    data,addr = s.recvfrom(1024)
    data = st.unpack(data)  # 数据解析  Struct模块的对象

    info = "%d  %s  %d  %.2f\n"%(data[0],\
                               data[1].decode(),data[2],data[3],)
    print(info[1])
    f.write(info)

f.close()
s.close()



