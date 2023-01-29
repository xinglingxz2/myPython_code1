'''
 文件读写测试1
'''


import os

#if __name__ == "__main__":

# print("获取当前文件路径——" + os.path.realpath(__file__))  # 获取当前文件路径
#
# parent = os.path.dirname(os.path.realpath(__file__))
# print("获取其父目录——" + parent)  # 从当前文件路径中获取目录
#
# garder = os.path.dirname(parent)
# print("获取父目录的父目录——" + garder)
# print("获取文件名" + os.path.basename(os.path.realpath(__file__)))  # 获取文件名
#

#===============================================
file1 = open("C:/Users/Administrator/PycharmProjects/untitled2/common/mytext1.txt","rb+") # 加 b 为字节串 形式
file1.write(b"hello world9981  \n")   # 加 b 为字节串 形式
print("当前文件偏移量：",file1.tell())
file1.seek(-18,1)  #   参1：正加负退   参2：（ 0 文件头，1当前位置，2末尾位置）
print("当前文件偏移量：",file1.tell())
while True:
    data = file1.readline()
    if not data:
        break
    print(data.decode())

print(os.path.getsize("mytext1.txt"))  #获取文件大小
print(os.listdir(".."))  #查看文件列表
print(os.path.isfile("mytext1.txt"))  #判定文件是否为普通文件
print(os.path.exists("mytext1.txt"))  #判定文件是否存在
os.remove()  # 删除文件

