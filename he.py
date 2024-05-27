class Asko:
    def __init__(self, name):
        self.n = name

    def info(self):
        return self.n

class Nursultan(Asko):
    def __init__(self):
        super().__init__("Nursulan")
        
class Arzygul(Asko):
    def __init__(self):
        super().__init__('Arzygul')

p = Arzygul()
print(p.info())
print('test')


class DONIKO312(Asko):
    def __init__(self):
        super().__init__('Daniel')

a = DONIKO312()
print(p.info())
