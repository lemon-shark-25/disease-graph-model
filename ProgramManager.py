import time
from GraphManager import GraphManager

DAYLIMIT = 100

class ProgramManager:



    def __init__(self):

        self.GM = GraphManager()
        self.Days = DAYLIMIT


    def start(self):

        self.GM.loadGraph()
        
        self.program()



    def program (self):

        while self.Days >= 0:  # mientras sea mayor o igual a 0

            self.GM.recorer()

            self.GM.showGraph()

            time.sleep(3)

              
            self.Days = self.Days -1
