
'''

'''

import os
import time
import random  # 随机数据  // random.randint(0,9)


os.system("clear")  # 清屏

time.sleep(3)  # 等待 ？秒

def fun00(a,b,c):
    print("a = %d, b = %d, c = %d,"%(a,b,c))

fun00(*[4,5,6])