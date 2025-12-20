import random
import re

class Person():
    def __init__(self, name, age):
        
        self._name = name
        self._age = age
        self._alive = True
        self._infected = False
        self._inmune = False
        self._multDeath = None
        self._multRecover = None
        self._multInfected = None
        self._mulInfect = None
        self._infectedCheck = False
        self._previousillness = False
        self._treated = False
        self._compliesRegulations= False

        self.start()

    def start (self):

        prob_seguir_normas = 60  # 60%
        sigue_normas = random.randint(0, 100) 

        if (sigue_normas > prob_seguir_normas):
                self._compliesRegulation = False
        elif    (sigue_normas < prob_seguir_normas):  
                 self._compliesRegulation = True
            
        prob_recibir_tratamiento = 87  # 87%
        recibe_tratamiento = random.randint(0, 100) 

        if (recibe_tratamiento > prob_recibir_tratamiento):
                    self._treated = False
        elif    (recibe_tratamiento < prob_recibir_tratamiento):  
                    self._treated = True

        prob_Enfermedad_Anterior = 16  # 87%
        tiene_Enfermedad = random.randint(0, 100) 

        if (tiene_Enfermedad > prob_Enfermedad_Anterior):
                    self._previousillness = False
        elif    (tiene_Enfermedad < prob_Enfermedad_Anterior):  
                    self._previousillness = True


        with open("./data/Probabilidad.txt", "r", encoding="utf-8") as f:
            for linea in f:
                linea = linea.strip()
                if not linea:  # saltar líneas vacías
                    continue

                # Tomar lo que está después de los dos puntos
                partes = linea.split(":", 1)
                if len(partes) < 2:
                    continue
                valor = partes[1].strip()  # eliminar espacios

                # Quitar el símbolo de porcentaje si existe
                if valor.endswith("%"):
                    valor = valor[:-1].strip()

                # Convertir a float
                try:
                    valor_num = float(valor)
                except ValueError:
                    continue

                # Llamar a la función correspondiente según el símbolo
                if linea.startswith("-"):
                    self.set_multDeath(valor_num)
                elif linea.startswith("+"):
                    self.set_multRecover(valor_num)
                elif linea.startswith("*"):
                    self.set_multInfected(valor_num)
                elif linea.startswith(">"):
                    self.set_mulInfect(valor_num)


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
        if not self._inmune:
            self._infected = True


    def set_multDeath(self, value):
             
            if self._previousillness:
                if self._treated:
                    m = ((value * self._age)*3.85)
                    self._multDeath = m - ((m*80)/100)
                else :
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
                else :
                    self._multRecover = ((value * self._age)*3.85)
            elif self._treated:   
                    c = (value * self._age)
                    self._multRecover = m + ((m*80)/100)  
            else:
                 self._multRecover = (value * self._age)


    def set_multInfected(self, value):
            
            if self._inmune:
             self._multInfected  = value / 3    
            else :
             self._multInfected  = value


    def set_mulInfect(self, value):
        
        if  self._compliesRegulations:
            self._mulInfect = value / 3
        else :
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
    
