
#-*- coding: UTF-8 -*-    """  coding=UTF-8    """
'''

'''
import pymysql
import sysconfig
import sys

class StuModelr: #学生类
    '''
      创建学生对象
      ：:param score:成绩
    '''
    #类变量 = 20
    def __init__(self,name="",age=0,score=0,id=0):
        self.name = name
        self.age = age
        self.score = score
        self.id = id

    @property    #属性
    def name(self):   #与实例变量名同名的方法名  print("这是属性保护的实例读方法————")
        return self.__name
    @name.setter  # 可能必须
    def name(self,value):
        self.__name =value

    @property    #属性
    def age(self):   #与实例变量名同名的方法名  print("这是属性保护的实例读方法————")
        return self.__age
    @age.setter  # 可能必须
    def age(self,value):
        self.__age =value

    @property    #属性
    def score(self):   #与实例变量名同名的方法名  print("这是属性保护的实例读方法————")
        return self.__score
    @score.setter  # 可能必须
    def score(self,value):
        self.__score =value

    @property    #属性
    def id(self):   #与实例变量名同名的方法名  print("这是属性保护的实例读方法————")
        return self.__id
    @id.setter  # 可能必须
    def id(self,str):
        self.__id =str


#----------------------------------------------#
    '''
    @classmethod     #类方法  通过类名调用,能调用类变量，不能调用实例变量
    def dosom(cls):
        print("我是类方法，我有类变量，它等于%d。 \n"%(cls.类变量))

    @staticmethod   #静态方法
    def fun02():
        print("我是静态方法。")
   '''
################################################
class StuManagerController:
    '''
    学生管理控制系统
    '''
    def __init__(self):  #
        self.__list_stu=[]  # 输入的是列表

    @property
    def list_stu(self):
        return self.__list_stu[:]  # 返回一个列表新的复制

    def add_stu(self,stu):   #参数：学生对象  ctrl +alt +M :提取方法
        id = self.__generate_id()
        stu.id = id
        self.__list_stu.append(stu)   # 列表 内 添加的是stu （学生类的对象）

    def __generate_id(self):
        # if len(self.__list_stu) > 0:
        #     id = self.__list_stu[-1].id + 1  # id自动增加1    #调试:shift +alt +F9     F7
        #
        #      # 学生对象[-1]:最后一个学生：的id +1
        # else:
        #     id = 1
        # return id
        return (self.__list_stu[-1].id + 1) if (len(self.__list_stu) > 0) else  1  # 满足条件返回值   条件  不满足返回值

    def update_stu(self,stu):
        '''
           修改学生学习，
        :return:
        '''
        #学生的数据都在列表内
        for item in self.__list_stu:  # 遍历
            if item.id == stu.id:
                item.name = stu.name
                item.age = stu.age
                item.score = stu.score
                return  True
        return False

# stuController = stuManagerController()
# stuController.add_stu(StuModelr("张三",18,85))
# for item in stuController.list_stu:
#     print(item.id,item.name)

class ViewManager:
    ''' 界面视图类  '''
    #@classmethod
    def __init__(self):
         self.__stuController = StuManagerController()   # 调用类 用（）


    def __input_stu(self):
        mName = input("请输入学生姓名： ")
        mAge =int(input("请输入学生年龄： "))
        mScore = int(input("请输入学生成绩： "))
        stuA=[mName,mAge,mScore]
        stu = StuModelr(mName,mAge,mScore)

        self.__stuController.add_stu(stu)
        for item in self.__stuController.list_stu:
             print(item.id,item.name,item.score)

    def __display_menu(self):

        print("-"*28)
        print("   (1)  添加学生")
        print("   (2)  显示学生")
        print("   (3)  删除学生")
        print("   (4)  修改学生")
        print("-"*28)

    def __select_menu(self):
        number = input("请输入选项号码： ")
        if number =="1":
            self.__input_stu()
        elif number =="2":
            pass

        elif number =="4":
            self.__modify_student()

    def __modify_student(self):

        stu = StuModelr()  # 建立学生对象
        stu.id = int(input("请输入学生编号："))
        stu.name =input("请输入学生姓名：")
        stu.age = input("请输入年龄：")
        stu.score =input("请输入学生考试成绩：")
        if self.__stuController.update_stu(stu) :   # 调用 控制类 的修改方法
            print("修改成功")
        else:
            print("修改失败")
        return stu

    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()

view = ViewManager()  #启动
view.main()
