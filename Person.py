import random

class Person():
    def __init__(self, name, age):
        
        self._name = name
        self._age = age
        self._alive = True
        self._infected = False
        self._alreadyinfected = False
        self._multDeath = random.randint(0, 10)
        self._multRecover = random.randint(0, 10)
        self._multInfected = random.randint(0, 10)
        self._mulInfect = random.randint(0, 10)
        self._infectedCheck = False
        self._infectedCounter = 0
        self._fullyIncubated = False
        self._INCUBATION_AVEREGE=5

    def die(self):

        muereOno= random.randint(0, 100) 

        if (muereOno > self._multDeath):
                    self._alive = True
        elif    (muereOno < self._multDeath): 
                    self._alive = False

    def recover(self):
        seCuraOno= random.randint(0, 100) 

        if    (seCuraOno < self._multRecover): 
                     self._infected = False
        else:
            self._multRecover = self._multRecover + 10   

    def contractDisease(self):
         
     #   if not self._inmune:
            self._infected = True

    def set_multDeath(self, value):
             
        if self._previousillness:
            if self._treated:
                m = ((value * self._age)*3.85)
                self._multDeath = m - ((m*80)/100)
            else:
                self._multDeath = ((value * self._age)*3.85)
        elif self._treated:   
            c = (value * self._age)
            self._multDeath = m - ((m*80)/100)  
        else:
            self._multDeath = (value * self._age)    

    def set_multRecover(self, value):
            if self._previousillness:
                if self._treated:
                    m = ((value * self._age)*3.85)
                    self._multRecover = m + ((m*80)/100)
                else:
                    self._multRecover = ((value * self._age)*3.85)
            elif self._treated:   
                c = (value * self._age)
                self._multRecover = m + ((m*80)/100)  
            else:
                self._multRecover = (value * self._age)


    def set_multInfected(self, value):
        if self._inmune:
            self._multInfected  = value / 3    
        else:
            self._multInfected  = value


    def set_mulInfect(self, value):
        if  self._compliesRegulations:
            self._mulInfect = value / 3
        else:
            self._mulInfect = value



    # Getters for private attributes (if needed for access outside of class)
    def get_name(self):
        return self._name
    
    def get_age(self):
        return self._age
    
    def is_alive(self):
        return self._alive

    def is_infected(self):
        return self._infected
    
    #def _postinfected(self): 
       # self._mulInfect= self._mulInfect*(1-ALREADY_INFECTED_REDUCTION)

    
