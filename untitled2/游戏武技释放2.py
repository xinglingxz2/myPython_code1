
# '''
#    游戏武技效果释放2.py  // 通过生成器 释放
#    C:\Users\Administrator\PycharmProjects\
# '''

class ImpactEffect:
    '''
       影响效果  (中间隔离类)
       隔离技能释放器 与 具体的影响效果
    '''
    def impact(self):
        # 要求子类必须实现，否则报错
        raise NotImplementedError()


class LowerDefense (ImpactEffect):  # 降低防御力
    '''
        降低防御力
    '''
    def __init__(self,distance, ratio): # 范围有效值，降低比例
        self.distance = distance
        self.ratio = ratio
    def impact(self):
        print("降低防御力，具体数值=%d"%(self.distance * self.ratio))

class LowerSpeed (ImpactEffect):
    '''
        降低速度
    '''
    def __init__(self,distance, ratio): # 速度值，降低比例
        self.distance = distance
        self.ratio = ratio
    def impact(self):
        print("降低速度，具体数值=%d"%(self.distance * self.ratio))


class Damage (ImpactEffect):
    '''
        降低生命值
    '''
    def __init__(self,value): # 降低血值
        self.value = value
    def impact(self):
        print("降低生命值，具体数值=%d"%(self.value))

##############################################

class SkillDeployer:
    '''
        技能释放器
    '''
    def __init__(self,name):
        self.name = name
        # 存储当前所有技能具有的 影响效果 对象
        # self.list_impact = self.config_deployer()  #调用本类内的 配置释放器 （老版本用）

        self.list_impact_out = self.get_skill(self.config_deployer())  #调用本类内的 配置释放器

    def config_deployer(self):
        # 配置释放器
        # 定义配置
        #1) 读取配置文件，得到相应的影响效果
           #功夫字典   具体游戏 可以是 游戏技能配置 文件
        dict_skill_config = {
            "无相神功":["LowerDefense(20,6)","Damage(10)"],
            "降龙十八掌":["LowerSpeed(40,9)","Damage(30)"],
            "如来神掌":["LowerSpeed(100,5)","LowerDefense(90,8)","Damage(120)"],
            "六脉神剑":["LowerSpeed(30,9)","LowerDefense(50,3)""Damage(70)"],
            "一剑出天门":["LowerSpeed(90,10)","Damage(20)"],
        }
        # 获取【（输入的对象名 = 功夫字典 内的 键名）相对应的值（列表值）】给 列表：影响效果 的名称
        list_impact_name = dict_skill_config[self.name]  #  通过输入的参数名，找到功夫字典内对应的 运行数据。 列表类型

        # #2）创建影响效果对象  （老版本用）
        # list_impact_out = []  # 创建空列表（
        # for item in list_impact_name:  #遍历列表元素
        #     list_impact_out.append(eval(item))   # 根据列表值，创建影响效果对象，保存到新列表中
        #        # eval() 函数功能： 把字符串 转义到 可执行命令
        # return list_impact_out

        return list_impact_name




    def get_skill(self,target):   # 2）创建影响效果对象（生成器）
        for item in target :
            yield eval(item)   # eval() 函数功能： 把字符串 转义到 可执行命令



    def generate_skill(self):
        # 生成技能
        # for item in self.list_impact:    # （老版本用）
        #     item.impact()   # 调用 影响效果 子类 的实现 （多态）
        for item in self.list_impact_out:
            item.impact()

#------------  测试  -------------------------

# if __name__ == ["__main__"] :
#     view = SkillDeployer()
#     view.main()

xiangLong18 = SkillDeployer("降龙十八掌")
xiangLong18.generate_skill()
rulai = SkillDeployer("如来神掌")
rulai.generate_skill()

