class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.alive = True
        self.infected = False
        self.inmune = False
        

    def die(self):
        self.alive = False

    def recover(self):
        self.infected = False

    def contractDisease(self):
        if not self.inmune:
            self.infected = True

