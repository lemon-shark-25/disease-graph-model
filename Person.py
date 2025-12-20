import random

class Person():
    def __init__(self, name, age):
        
        self._name = name
        self._age = age
        self._alive = True
        self._infected = False
        self._inmune = False
        self._multDeath = random.randint(0, 10)
        self._multRecover = random.randint(0, 10)
        self._multInfected = random.randint(0, 10)
        self._mulInfect = random.randint(0, 10)
        self._infectedCheck = False

    def die(self):
        self._alive = False

    def recover(self):
        self._infected = False

    def contractDisease(self):
        if not self._inmune:
            self._infected = True

    # Setters for multipliers
    def set_multDeath(self, value):
        if isinstance(value, int) and 0 <= value <= 10:
            self._multDeath = value
        else:
            print("Invalid value for multDeath. It should be an integer between 0 and 10.")

    def set_multRecover(self, value):
        if isinstance(value, int) and 0 <= value <= 10:
            self._multRecover = value
        else:
            print("Invalid value for multRecover. It should be an integer between 0 and 10.")

    def set_multInfected(self, value):
        if isinstance(value, int) and 0 <= value <= 10:
            self._multInfected = value
        else:
            print("Invalid value for multInfected. It should be an integer between 0 and 10.")

    def set_mulInfect(self, value):
        if isinstance(value, int) and 0 <= value <= 10:
            self._mulInfect = value
        else:
            print("Invalid value for mulInfect. It should be an integer between 0 and 10.")

    # Getters for private attributes (if needed for access outside of class)
    def get_name(self):
        return self._name
    
    def get_age(self):
        return self._age
    
    def is_alive(self):
        return self._alive

    def is_infected(self):
        return self._infected
    
    def _getNodeColors(self):
    colors = []

    for person in self.G.nodes:
        if not person._alive:
            colors.append("black")
        elif person._infected:
            colors.append("red")
        elif person._inmune:
            colors.append("blue")
        else:
            colors.append("green")

    return colors

