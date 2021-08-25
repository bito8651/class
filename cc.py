
class Player:
    def __init__(self, name, atk):
        print('我誕生了')
        self.name = name
        self.hp = 100
        self.atk = atk  # 左邊是屬性 右邊是參數

    def attack(self, target):
        print(self.name, 'attacks', target.name)  # target一定要是Player這個class裡的物件
        target.hp = target.hp - self.atk


p1 = Player('Player1', 5)
p2 = Player('Player2', 10)
p1.attack(p2)
print(p2.hp)
