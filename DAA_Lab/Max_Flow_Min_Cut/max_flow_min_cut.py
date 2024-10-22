from typing import Dict
from itertools import combinations
from math import pow
from copy import deepcopy

class Graph:
    
    def __init__(self) -> None:

        self.graph : Dict[int, list[int | bool]] = {}
        
        self.source_vertex = None
        self.sink_vertex = None
        
        self.all_edges = []
        self.all_edge_combinations = []

        self.stack : list[int] = []
        self.visited : list[list[int]] = []

        self.logs = []

    def add_edge(self, source_vertex : int, destination_vertex : int, weight : int) -> None:

        if(source_vertex not in self.graph):
            self.graph[source_vertex] = [[destination_vertex, weight, False]]
        else:
            if([destination_vertex, weight, False] not in self.graph[source_vertex]):
                self.graph[source_vertex].append([destination_vertex, weight, False])
    
    def display_graph(self) -> None:

        for key, values in self.graph.items():
            print(f"{key} : {values}")
    
    def set_source_vertex(self, source_vertex : int) -> None:
        self.source_vertex = source_vertex

    def set_sink_vertex(self, sink_vertex : int) -> None:
        self.sink_vertex = sink_vertex
    
    def generate_all_edges(self) -> None:
        
        for key, values in self.graph.items():
            
            for vertex in values:
                self.all_edges.append([key, vertex[0]])

    def generate_all_edge_combinations(self):
        
        for i in range(1, len(self.all_edges) + 1):
            temp_edge_list = list(combinations(self.all_edges, i))
            
            for edge in temp_edge_list:
                self.all_edge_combinations.append(list(edge))
    
    def get_destination_vertex_index(self, edge : list[int]):
        
        i : int = 0
        while(i < len(self.graph[edge[0]])):
            
            if(self.graph[edge[0]][i][0] == edge[1]):
                return i

            i += 1

    def block_edges(self, edge_combination : list[list[int]]) -> None:
        
        for edge in edge_combination:
            
            destination_index = self.get_destination_vertex_index(edge)
            self.graph[edge[0]][destination_index][2] = True

    def unblock_edges(self, edge_combination : list[list[int]]) -> None:
        
        for edge in edge_combination:
            
            destination_index = self.get_destination_vertex_index(edge)
            self.graph[edge[0]][destination_index][2] = False

    def find_exit_points(self, current_pointer) -> list[int]:
        
        exit_points : list[int] = []

        for destination_vertex in self.graph[current_pointer]:

            if(not destination_vertex[2] and [current_pointer, destination_vertex[0]] not in self.visited):
                exit_points.append(destination_vertex[0])

        return exit_points



    def check_path(self) -> bool:
        
        self.stack = []
        self.visited = []

        current_pointer = self.source_vertex
        while(current_pointer != self.sink_vertex):
            
            exit_points = self.find_exit_points(current_pointer)

            if(len(exit_points) == 0):    
                
                if(len(self.stack) != 0):
                    current_pointer = self.stack.pop()
                else:
                    return False

            elif(len(exit_points) == 1):
                
                popped_vertex = exit_points.pop(0)
                self.visited.append([current_pointer, popped_vertex])
                current_pointer = popped_vertex

            elif(len(exit_points) > 1):
                
                self.stack.append(current_pointer)
                popped_vertex = exit_points.pop(0)
                self.visited.append([current_pointer, popped_vertex])
                current_pointer = popped_vertex

        return True


    def calculate_weight(self, edge_combination : list[list[int]]) -> int:

        weight = 0

        for edge in edge_combination:
            
            destination_index = self.get_destination_vertex_index(edge)
            weight += self.graph[edge[0]][destination_index][1]

        return weight

    def calculate_maximum_flow(self) -> int:
        
        minimum_weight = int(pow(2, 31))

        self.generate_all_edges()
        self.generate_all_edge_combinations()

        for edge_combination in self.all_edge_combinations:
            self.block_edges(edge_combination)
            
            if(not self.check_path()):
                
                weight = self.calculate_weight(edge_combination)
                if(weight < minimum_weight):
                    minimum_weight = weight
                    self.logs.append([weight, deepcopy(self.graph)])


            self.unblock_edges(edge_combination)
        
        return minimum_weight

def main():
    
    g1 : Graph = Graph()

    g1.add_edge(1, 2, 11)
    g1.add_edge(1, 3, 12)
    g1.add_edge(2, 4, 12)
    g1.add_edge(3, 2, 1)
    g1.add_edge(3, 5, 11)
    g1.add_edge(4, 6, 19)
    g1.add_edge(5, 4, 7)
    g1.add_edge(5, 6, 4)

    # Ans : 23

    # g1.add_edge(1, 2, 6)
    # g1.add_edge(1, 3, 6)
    # g1.add_edge(2, 4, 4)
    # g1.add_edge(2, 5, 3)
    # g1.add_edge(3, 4, 3)
    # g1.add_edge(3, 5, 4)
    # g1.add_edge(4, 6, 5)
    # g1.add_edge(5, 6, 5)

    # Ans : 10

    # g1.add_edge(1, 2, 9)
    # g1.add_edge(1, 3, 8)
    # g1.add_edge(2, 4, 4)
    # g1.add_edge(2, 5, 4)
    # g1.add_edge(3, 2, 2)
    # g1.add_edge(3, 5, 5)
    # g1.add_edge(3, 6, 3)
    # g1.add_edge(4, 6, 5)
    # g1.add_edge(5, 6, 6)

    # Ans : 13

    # g1.add_edge(1, 2, 10)
    # g1.add_edge(1, 3, 5)
    # g1.add_edge(1, 4, 15)
    # g1.add_edge(2, 3, 4)
    # g1.add_edge(2, 5, 9)
    # g1.add_edge(2, 6, 15)
    # g1.add_edge(3, 4, 4)
    # g1.add_edge(3, 6, 8)
    # g1.add_edge(4, 7, 30)
    # g1.add_edge(5, 6, 15)
    # g1.add_edge(5, 8, 10)
    # g1.add_edge(6, 7, 15)
    # g1.add_edge(6, 8, 10)
    # g1.add_edge(7, 3, 6)
    # g1.add_edge(7, 8, 10)

    # Ans : 28


    # g1.add_edge(1, 2, 5)
    # g1.add_edge(1, 3, 1)
    # g1.add_edge(2, 4, 1)
    # g1.add_edge(3, 2, 10)
    # g1.add_edge(3, 4, 5)

    # Ans : 2
    
    g1.set_source_vertex(1)
    g1.set_sink_vertex(6)

    maximum_flow : int = g1.calculate_maximum_flow()
    print(f"Maximum flow through the network is : {maximum_flow}")
    
    # for e in g1.logs:
    #     print(e)
    
if(__name__ == "__main__"):
    print()
    main()
    print()
