class Pet:
    def __init__(self):
        self.name = "NoName"
        self.age = 0

    def setName(self, n):
        self.name = n

    def setAge(self, a):
        self.age = a

    def status(self):
        print("Name : %s" % self.name)
        print("Age  : %d" % self.age)

    def sound(self):
        pass


class Dog(Pet):
    def __init__(self):
        super().__init__()
    
    def run(self):
        print("Run Run Run")
    
    def sound(self):
        print("bark!")

class Cat(Pet):
    def __init__(self):
        super().__init__()
    
    def jump(self):
        print("Jump Jump Jump")
    
    def sound(self):
        print("mew!")

d = Dog()
d.setName("Ben")
d.setAge(3)
d.status()
d.sound()
d.run()
print("======================")
c = Cat()
c.setName("Aslan")
c.setAge(2)
c.status()
c.sound()
c.jump()

class PersianCat(Cat):
    def __init__(self):
        super().__init__()
    
    def setName(self, n):
        self.name = "Persian " + n

print("======================")
p = PersianCat()
p.setName("Simba")
p.setAge(10)
p.status()
p.jump()