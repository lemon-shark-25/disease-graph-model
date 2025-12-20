from GraphManager import GraphManager

class ProgramManager:


    def __init__(self):
        self.GM = GraphManager()
        


    def start(self):

        self.GM.loadGraph()
        self.GM.showGraph()


