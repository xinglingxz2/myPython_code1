"""

"""
# 自定义异常
class StackError(Exception):
    pass

# 基于列表实现顺序
class SStack:
    def __init__(self):
        self._elems = []  #列表的最后一个元素为栈顶

    # 显示栈顶最新添加的元素
    def top(self):
        if not self._elems:
            raise StackError("stack is empty")
        return self._elems[-1]

    # 判定栈是否为空
    def is_empty(self):
        return  self._elems == []

    # 入栈
    def push(self,elem):
        self._elems.append(elem)

    # 出栈
    def pop(self):
        if not self._elems:
            raise StackError("stack is empty")
        return self._elems.pop()


#  ============================================================
if __name__ == "__main__":
    st = SStack()  # 初始化栈
    print(st.is_empty())
    st.push(10)
    st.push(20)
    st.push(30)
    while not st.is_empty():
        print(st.pop())

# data = "get(键，默认值) //有 返回键对应值，无 返回默认值has_key(键)  " \
#        "//判断字典中是否有 键。in 和 not in 替items()  //返回键值对元组的列表keys()  " \
#        " //返回字典中键的列表iter*(); .iteritems(); iterkeys();itervalues()." \
#        "pop（键[默认值]）//有( (返回删除键对应值，无默认值setdefault(键，默认值) //有 返回键对应值，无新建 键=默认值"
#
# noba = SStack()
# n =0
# for item in data:
#     if item =='('or item==')':
#         n += 1
# print(n)
# if n%2 ==1 :
#     print(False)
# else:
#     print(True)