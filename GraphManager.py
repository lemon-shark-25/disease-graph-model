import networkx as nx
import matplotlib.pyplot as plt
from Person import Person

class GraphManager():

    def __init__(self):
        self.G = nx.Graph()
        self.time = 0

    def loadPerson(self):
        pass

    def loadProvisional(self):
        persons = []

        # Crear personas y añadirlas como nodos
        for i in range(10):
            p = Person(i, i * 10 + 1)
            persons.append(p)
            self.G.add_node(p)

        # Conectar todas las personas entre sí
        for i in range(len(persons)):
            for j in range(i + 1, len(persons)):
                self.G.add_edge(persons[i], persons[j], weight=0.2)

    def showGraph(self):
        nx.draw_circular(self.G, with_labels=False)
        plt.show()
