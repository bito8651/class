# class 類別(種類)
# x = 5  x is  the name of this class int(object), its value is 5.
# type() is used to ask what class of this object.
# objects 有attributes(屬性)
# dir() is used to ask what attributes that this objects has.
# class is used to 建立/發明自己的類別
# 好處有三：1️⃣把相關function收納在一起2️⃣透過self來共用身上的屬性3️⃣包裝程式碼 方便使用
# 也可以使用inheritance繼承

class Student:
    def __init__(self, name, score):  # init : initialize 初始化 用來做該物件的初始設定
        self.name = name  # 用設值指令創造出這個屬性 # 等號右邊的name是上一行第二個參數的name
        self.score = score
        print('我誕生了')
        self.do_hw('英文')
        self.study()
        self.sleep()

    def do_hw(self, hw):
        print('我在做作業', hw)

    def study(self):
        print('我在讀書')
        self.score += 5

    def sleep(self):
        print('I am sleeping!')


s1 = Student('Chloe', 96)
s2 = Student('Riley', 74)
students = [s1, s2]
for s in students: # for loop is to call the object in the list one by one
    print(s.name, '的分數是', s.score)
# print(s1.name, s1.score)
# print(s2.name, s2.score)
# s2.study()
# print(s2.name, s2.score)
