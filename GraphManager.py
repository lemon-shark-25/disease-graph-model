import networkx as nx # type: ignore
import matplotlib.pyplot as plt # type: ignore
import csv
from Person import Person

class GraphManager():

    def __init__(self):
        self.G = nx.Graph()
        self.time = 0

    def _loadNodes(self, path):
        """
        Carga personas desde CSV y devuelve un diccionario {id: Person}
        """
        persons = {}

        with open(path, newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                pid = int(row["id"])
                person = Person(row["nombre"], int(row["edad"]))

                persons[pid] = person
                self.G.add_node(person)

        return persons


    def _loadEdges(self, path, persons):
        """
        Carga aristas desde CSV usando los IDs de persons
        """
        with open(path, newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                n1 = int(row["nodo1"])
                n2 = int(row["nodo2"])
                weight = float(row["peso"])

                # Validación mínima
                if n1 not in persons or n2 not in persons:
                    continue

                self.G.add_edge(persons[n1], persons[n2], weight=weight)

    def loadGraph(self):
        """
        Método principal de carga del grafo
        """
        persons = self._loadNodes("./data/nodes.csv")
        self._loadEdges("./data/edges.csv", persons)

    def showGraph(self):
        nx.draw(self.G, with_labels=False)
        plt.show()


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
