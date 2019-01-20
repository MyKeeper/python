'''
定义一个学生类，用来形容学生
'''


# 定义一个空的类
class Student():
    # 一个空类 pass代表直接跳过
    # pass 必须有
    pass


# 定义一个对象
mingyue = Student()


# 在定义一个类 用来描述学Python的学生
class PythonStudent():
    # 使用none给不确定的值赋值
    name = None
    age = 18
    course = "python"

    # 注意缩进
    # 系统默认有一个self参数
    def doHomework(self):
        print("i am dong homework")
        # 推荐在函数结尾使用return语句
        return None


# 实例化一个叫yueyue的学生 是一个具体的人
yueyue = PythonStudent()
print(yueyue.name)
print(yueyue.age)
# 注意成员函数的调用没有传递参数
yueyue.doHomework()

