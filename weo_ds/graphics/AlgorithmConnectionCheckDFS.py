from Graph import Graph


class AlgorithmConnectionCheckDFS:
    def __init__(self, g: Graph):
        self.graph = g
        self.searched_mark = [0] * g.get_vertex_count()
        self.connected_mark = [0] * g.get_vertex_count()
        self.connected_component_count = 0

        for vertex in range(self.graph.get_vertex_count()):
            if self.searched_mark[vertex] == 0:
                self.connected_component_count += 1
                self.dfs(vertex, self.connected_component_count)

    def dfs(self, start_vertex: int, mark: int):
        self.searched_mark[start_vertex] = 1
        self.connected_mark[start_vertex] = mark

        for adj_vertex in self.graph.get_adjacent_vertex(start_vertex):
            if self.searched_mark[adj_vertex] == 0:
                self.dfs(adj_vertex, mark)

    def get_if_connected(self, v1: int, v2: int):
        return self.connected_mark[v1] == self.connected_mark[v2]

    def get_components_count(self):
        return self.connected_component_count
