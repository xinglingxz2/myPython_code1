'''
ftp文件服务器:  1.服务器端  功能：查看服务器端文件， 下载，上传
分析：  1网络搭建  2查看库信息   3下载  4上传  5客户端退出

'''

#

import ctypes

import multiprocessing
import os

def runchildProcess(name):
    pass


if __name__ == '__main__':   # windows系统必须添加  执行从这里开始
    print("=="*20)
    child = multiprocessing.Process(target=runchildProcess,args=('test',))
    child.start()
    child.join()
