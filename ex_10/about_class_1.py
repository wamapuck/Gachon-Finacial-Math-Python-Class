class Fruit:
    def __init__(self, color, type):
        self.color = color
        self.type = type
    
    def show(self):
        print(f"TYPE: {self.type}, COLOR: {self.color}")

s1 = Fruit("Yellow", "fig")
s2 = Fruit("Red", "Apple")

s1.show()
s2.show()