class Graph:

    def __init__(self):
        self.graph = dict()

    def add_vertex(self, vertex):
        self.graph[vertex] = []

    def add_edge(self, vertex_1, vertex_2, weight):
        self.graph[vertex_1].append([vertex_2, weight])

    def display(self):

        for key, value in self.graph.items():
            print(key, ":", value)

def main():
    
    g1 = Graph()
    g1.add_vertex(1)
    g1.add_vertex(2)
    g1.add_vertex(3)
    g1.add_vertex(4)
    g1.add_vertex(5)
    g1.add_vertex(6)

    g1.add_edge(1, 2, 11)
    g1.add_edge(1, 3, 12)
    g1.add_edge(2, 4, 12)
    g1.add_edge(3, 2, 1)
    g1.add_edge(3, 5, 11)
    g1.add_edge(4, 6, 19)
    g1.add_edge(5, 4, 7)
    g1.add_edge(5, 6, 4)

    g1.display()


if(__name__ == "__main__"):
    print()
    main()
    print()