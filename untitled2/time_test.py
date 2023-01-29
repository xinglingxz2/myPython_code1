
import time

print(time.time()) # 时间戳

print(time.localtime())  #  当前时间元组

print(time.mktime(time.localtime()))   #  当前时间元组 --> 时间戳

print(time.strftime("%Y %m %d  %H: %M: %S",time.localtime())) # 当前时间串