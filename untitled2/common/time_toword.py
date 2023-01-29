import  time

# f = open("time.txt","a+")  # 打开文件
# f.seek(0)
# n =1
# for line in f:
# 	n +=1
# while True:
#     time.sleep(1)
#     s = "%d.  %s\n"%(n,time.ctime())
#     f.write(s)
#     f.flush()
#     n +=1

print(time.localtime(time.time()))
sTime = time.asctime( time.localtime( time.time()))
print(sTime)
# Tue Feb 17 10:28:39 2016  // 13:16:18
# 123456789012345678901234  //
strM = sTime[14:16]  # 获取分钟
strS = sTime[17:19]  # 获取秒