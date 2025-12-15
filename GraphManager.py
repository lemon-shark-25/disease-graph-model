import networkx as nx
import Person

class GraphManager():
    def __init__(self):
        time = 0
        G = nx.Graph()

    def loadPerson(self):
        pass

    def loadProvisional(self):
        nodes = [] 
        for i in range(9):
            nodes[i] = Person(i, i*10 + 1)

        self.G.add_nodes_from(nodes)

        for i in range(9):
            for j in range(9):
                self.add_edge(i, j, weight=0.2)

