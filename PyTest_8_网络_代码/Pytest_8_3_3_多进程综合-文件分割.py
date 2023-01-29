'''   基本成功   问题：
   多进程 综合练习1：  1文件 分割为2 文件
'''

from multiprocessing import Process
import time
import os

filename = "./wujing.jpeg"  # 指定文件
size = os.path.getsize(filename)  # 获取图片大小

# 复制上半部分
def topCopy():
    f = open(filename,'rb')  # 文件打开方式
    n = size/2
    fw = open("topWJ.jpeg",'wb') # 写入文件设定

    while True:
        data = f.read(1024)
        fw.write(data)
        nsize = os.path.getsize("./topWJ.jpeg")
        if nsize > size/2:
            break
        time.sleep(0.1)
    f.close()
    fw.close()
    print("   ......A")

# 复制下半部分
def botCopy():
    f =open(filename,'rb')
    fw= open("botWJ.jpeg",'wb')
    data = f.read(512)
    fw.write(data)
    f.seek(size // 2, 0)
    while True:
        data2= f.read(1024)
        if not data2:
            break
        fw.write(data2)
    f.close()
    fw.close()
    print("   ......B")

# 多进程
p1= Process(target=topCopy)
p2= Process(target=botCopy)
p1.start()
p2.start()
p1.join()
p2.join()
