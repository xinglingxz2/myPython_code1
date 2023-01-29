import time
import os


"""  游戏 2048 核心代码

     函数基本OK
"""

  # 方案1
def zero_to_end(list_target):
    # 从后往前判定，如果零元素，则删除，在末尾追加零元素
    # [2,0,2,0]  --> [2,2]   --> [ 2,2,0,0]
    for i in range(len(list_target) -1,-1,-1):
        if list_target[i] == 0:
             del list_target[i]
             list_target.append(0)


# list01 = [2,0,2,0]
# zero_to_end(list01)
# print(list01)

  # 练习2 ： 定义合并函数
  #   [2,2,0,0]  --> [4,0,0,0]
  #   [2,0,2,0]  --> [4,0,0,0]
  #   [2,0,0,2]  --> [4,0,0,0]
  #   [2,2,2,0]  --> [4,2,0,0]

def merge(list_target):
    # [2,0,2,0]  -->  [2,2,0,0]
    zero_to_end(list_target)
    # [2,2,0,0]  -->  [4,0,0,0]
    for i in range(len(list_target) - 1):
        # 相邻且相等
        if list_target[i] == list_target[i + 1]:
            list_target[i] += list_target[i + 1]
            list_target[i + 1] = 0
    zero_to_end(list_target)   # [4,0,2,0]  -->  [4,2,0,0]


# list01 = [2,2,2,0]
# merge(list01)
# print(list01)

# 练习3 ： 将二维列表，以表格的格式显示在控制台中
list01 = [
     [2,0,4,2],
     [2,2,0,0],
     [2,0,4,4],
     [4,0,0,2]
]

def print_map(map):
    for r in range(len(map)):
        for c in range(len(map[r])):
            print(map[r][c],end=" ")
        print()



#print_map(list01)

# 练习4： 定义向左移动函数
def move_left(map):
    # 获取第行
    for r in range(len(map)):
        # 从左往右获取行
        # 交给merge进行合并
        merge(map[r])


def move_right(map):
    # 获取第行
    for r in range(len(map)):
        # 从右往左获取行
        # 交给merge进行合并
        list_merge = map[r][::-1]
        merge(list_merge)
        map[r][::-1] = list_merge


# 定义向上移动函数
def move_up(map):
    for c in range(4):
         list_merge = []
         # 从上往下获取列，形成一位列表 (从左往右）
         for r in range(4):    # 0 1 2 3
             list_merge.append(map[r][c])
           # 交给合并方法
         merge(list_merge)
           # 将合并后的结果list_merge（从左往右），还原给二维列表
         for r in range(4):  # 0 1 2 3
             map[r][c] = list_merge[r]


# 定义向下移动函数
def move_down(map):
    for c in range(4):
        list_merge = []
        # 从上往下获取列，形成一位列表 (从左往右）
        for r in range(3,-1,-1): # 3  2  1  0
            list_merge.append(map[r][c])
        # 交给合并方法
        merge(list_merge)
        # 将合并后的结果list_merge（从左往右），还原给二维列表
        for r in range(3,-1,-1):  # 3 2 1 0
            map[r][c] = list_merge[3 - r]  # 0 1 2 3

#=======================================
print_map(list01)   # 显示出 表
print("=="*20)
move_up(list01)
print_map(list01)  # 显示出 表
print("=="*20)
time.sleep(1)
move_down(list01)
print_map(list01)    # 显示出 表


