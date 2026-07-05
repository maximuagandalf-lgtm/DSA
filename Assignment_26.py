class graph:
    def __init__(self, vno):
        self.vertex_count = vno
        self.adj_matrix = [ [0]*vno for e in range(vno)]
    
    def add_edge(self, u, v, weight = 1): #default weight is 1 in adjacency matrix.
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.adj_matrix[u][v] = weight
            self.adj_matrix[v][u] = weight
        else:
            raise IndexError("Invalid Vertex")
        
    def remove_edge(self, u, v):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.adj_matrix[u][v] = 0
            self.adj_matrix[v][u] = 0
        else:
            raise IndexError("Invalid Vertex")
        
    def has_edge(self, u, v):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            return self.adj_matrix[u][v] == self.adj_matrix[v][u] == 1
        else:
            raise IndexError("Invalid Vertex")
    
    def print_adj_matrix(self):
        for row_list in self.adj_matrix:
            print(" ".join(map(str,row_list)))

#driver_code
g1 = graph(5)
g1.add_edge(0,1)
g1.add_edge(1,2)
g1.add_edge(1,3)
g1.add_edge(2,3)
g1.add_edge(3,4)

g1.print_adj_matrix()

g1.remove_edge(2,3)

g1.print_adj_matrix()

print(g1.has_edge(3,4))
print(g1.has_edge(2,3))