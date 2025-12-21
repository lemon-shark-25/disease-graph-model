import networkx as nx # type: ignore
import matplotlib.pyplot as plt # type: ignore
import csv
from Person import Person

class GraphManager():
    
    def __init__(self):
        self._infected_total = 0
        self.G = nx.Graph()
        self.time = 0

        plt.ion()
        self.fig, self.ax = plt.subplots()

        self.pos = None  # posiciones fijas

    
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
        persons = self._loadNodes("./data/nodes.csv")
        self._loadEdges("./data/edges.csv", persons)

        # layout fijo (una sola vez)
        self.pos = nx.circular_layout(self.G)


    def showGraph(self):
        self.ax.clear()

        nx.draw(
            self.G,
            pos=self.pos,           # ⬅ círculo fijo
            ax=self.ax,
            node_color=self._getNodeColors(),
            with_labels=False
        )

        plt.pause(0.5)



    def _getNodeColors(self):
        colors = []

        for person in self.G.nodes:
            if not person._alive:
                colors.append("black")
            elif person._infected:
                colors.append("red")
            elif person._alreadyinfected:
                colors.append("blue")
            else:
                colors.append("green")

        return colors
    

    def get_infection_stats(self):
        infected_now = 0
        

        for nodo in self.G.nodes:
            if nodo._infected:
                infected_now += 1

        return infected_now
    def recorer(self):
        steps = 50

        for step in range(steps):

            for nodo in self.G.nodes:
                if nodo._alive:
                    nodo.contractDisease(self.G)
                    nodo.recover()
                    nodo.die()

            for nodo in self.G.nodes:
                nodo.infectedCheck()
                nodo.day_pased()

            actuales = self.get_infection_stats()
            print(f"Paso {step}: actuales={actuales}")

            self.showGraph()
