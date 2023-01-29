
# 异常 相关1 ：

class Except_myInput:
    def __input_int (self,msg):   # 输入异常 反馈处理  参数msg ：输入提示字符串
        while True:
            try:
                ret = int( input(msg)   )   #  return ret
            except:
                print("输入有错误，请重新输入：")
                continue        #
            if 0< ret <=100 :
                return  ret
            print("输入数据 不在要求范围内")

    '''
    try:
        可能出现异常的语句...
    except Exception as e :    # ValueError  //类型错误    ZeroDivisionError  //零值错误   （常用python异常类型）

    else:
    finally:
    '''







