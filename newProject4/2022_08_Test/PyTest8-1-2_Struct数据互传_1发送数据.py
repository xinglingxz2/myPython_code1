'''  Python教程 8-1-2
  Struct模块的对象:  发送数据(对外软件数据传输协议）
'''

from socket import *
import struct



ADDR = ('127.0.0.1',8888)    # 接收端地址
st = struct.Struct('i32sif')   # 规定数据格式  创建Struct模块的对象

s = socket(AF_INET,SOCK_DGRAM)  # 创建udp套接字

while True:
    print("="*20)
    id = int(input("ID:"))
    name = input("NAME:").encode()
    age = int(input("AGE:"))
    score = float(input("SCORE:"))

    data = st.pack(id,name,age,score)  # 数据打包  Struct模块的对象

    s.sendto(data,ADDR)

s.close()


