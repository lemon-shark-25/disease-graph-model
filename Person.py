import random
PROB_BASE = 0.05
class Person():
    def __init__(self, name, age):
        
        self._name = name
        self._age = age
        self._alive = True
        self._infected = True
        self._treated=True
        self._alreadyinfected = False
        self._multDeath = 0
        self._multRecover = 0
        self._multInfected = random.randint(0, 2)
        self._mulInfect = random.randint(0, 2)
        self._infectedCheck = False
        self._infectedCounter = 0
        self._fullyIncubated = False
        self._previousillness = False
        self._mask= True
        self._INCUBATION_AVEREGE=5
        self._daysinfected=0
        self._ill=False


    def die(self):
            
            P = 0.005 * self._multDeath
            if P > 1.0:
                P = 1.0

            if random.random() < P:
                self._alive = False

        
    def recover(self):
        seCuraOno = random.randint(0, 100)

        if seCuraOno < self._multRecover:
            self._infected = False

            if self._ill == True:
                self._mulInfect *= 2
                self._ill = False

            self._postinfected()
        else:
            self._multRecover += 10   

    

    def contractDisease(self, graph):
       
        if not self._alive or self._infected:
            return

        for neighbor in graph.neighbors(self):

           
            if not neighbor._alive or not neighbor._infected:
                continue

            
            edge_data = graph.get_edge_data(self, neighbor)
            weight = edge_data.get("weight", 1.0)

           
            P = (
                PROB_BASE
                * neighbor._mulInfect      
                * self._multInfected       
                * weight
            )

            
            if P > 1.0:
                P = 1.0

         
            if random.random() < P:
                self._infectedCheck = True
                GM._infected_total+=1
                return  

        
            

    def infectedCheck(self):

        if (self._infectedCheck == True):
            self._infected = True
            self._infectedCheck = False



    
             
    def set_multDeath(self):
            age_factor = 2 ** ((self._age - 50) / 8)
            if age_factor < 0.05:
                age_factor = 0.05

            illness_factor = 2.0 if self._previousillness else 1.0
            treatment_factor = 0.5 if self._treated else 1.0

            self._multDeath = age_factor * illness_factor * treatment_factor

 
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

   

    def set_mulInfect(self, value):
        if  self._mask:
            self._mulInfect = value
        else:
            self._mulInfect = value*2

    def _postinfected(self): 
             self._multInfected *= (1 - 0.4)

    def _dayspassed(self):
            if self._daysinfected>=  self._INCUBATION_AVEREGE:
                self._mulInfect=self._mulInfect*0,5
                self._ill= False

    def get_name(self):
        return self._name
    
    def get_age(self):
        return self._age
    
    def is_alive(self):
        return self._alive

    def is_infected(self):
        return self._infected
    
    def day_pased(self):
         self._daysinfected+=1
    
