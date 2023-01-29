'''  broadcast_recv.py
    广播发送
'''
import os
import time
from socket import *

s = socket(AF_INET,SOCK_DGRAM)
s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)  # 让套接字可以接收广播

data = """
        **************************
            2022  08-16  小雨
         天街小雨润如酥，草色遥看近却无。
         最是一年春好处，绝胜烟柳满皇都。
        **************************

"""

while True:
   # sleep(2)
    s.sendto(data.encode(),dest)

s.close()