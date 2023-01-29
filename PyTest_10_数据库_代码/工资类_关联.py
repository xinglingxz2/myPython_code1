'''
  此程序使用的是关联，
  泛化：（继承）
  关联：B类为A类的成员数据
  依赖：B类为A类的方法的参数
  Employee  员工  ； salary  工资   ； job  岗位
'''

class 员工:
    def __init__(self,name,job):
        self.name = name
        self.job = job
    def 计数_工资(self):
        return self.job.get_工资()

#------------------------------------#
class Job:
    def __init__(self,基本工资):
         self.__基本工资 = 基本工资
    def get_工资(self):
         return self.__基本工资


#------------------------------------#
class 程序员(Job):
     def __init__(self,基本工资,岗位工资):
         super().__init__(基本工资)
         self.__岗位工资 = 岗位工资
     def get_工资(self):
         return super().get_工资() + self.__岗位工资

class 销售员(Job):
    def __init__(self,基本工资,岗位工资):
         super().__init__(基本工资)
         self.__岗位工资 = 岗位工资
    def get_工资(self):
         return super().get_工资() + int(self.__岗位工资* 0.5)

#====================================#

xl = 员工("小李",销售员(1000,5000))
print(xl.name + "每1月收入 = ",xl.计数_工资())

xl.job = (程序员(3000,5000))
print(xl.name + "每2月收入 = ",xl.计数_工资())