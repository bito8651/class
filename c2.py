class Desk:
    def __init__(self, color):
        self.color = color
        print('我被製造出來了～')

    def re_color(self, new_color):
        self.new_color = new_color

d = Desk('Blue')
print()