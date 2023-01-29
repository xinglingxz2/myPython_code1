#  001） 不用for循环，遍历字典，
#       根据字典的值，排序字典顺序

room = {"李白":105,"杜甫":108,"白居易":103}

aid=[]   # 定义空列表
aname=[]  # 定义空列表

def maxList (list1,list2):  #根据参数1值的大小， 排列参数2的顺序
    length = len(list1)
    for i in range(length - 1, 0, -1):
        for j in range(i):
            if list1[j] > list1[i]:
                list1[j], list1[i] = list1[i], list1[j]
                list2[j], list2[i] = list2[i], list2[j]
    return list2
#-------------------------------------------

iterator = room.__iter__()
while True:
    try:
        kev = iterator.__next__()
        print(kev,room[kev])


        aid.append(room[kev])
        aname.append(kev)

    except StopIteration:
        break
#==============================================

aname = maxList(aid,aname)
print(aname)

