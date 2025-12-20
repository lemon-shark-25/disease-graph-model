from GraphManager import GraphManager

class ProgramManager:


    def __init__(self):
        self.GM = GraphManager()
        self.Days = 100


    def start(self):

        self.GM.loadGraph()
        
        self.program()



    def program (self):

        while self.Days >= 0:  # mientras sea mayor o igual a 0

            self.GM.recorer()

            self.GM.showGraph()

            time.sleep(3)

              
            self.Days = self.Days -1
