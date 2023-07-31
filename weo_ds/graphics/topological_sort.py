
class Graph:
    def __init__(self, vertex_count: int):
        self.adj_list = [[] for _ in range(vertex_count)]
        self.edge_count = 0
        self.vertex_count = vertex_count

    def add_edge(self, v1: int, v2: int):
        self.adj_list[v1].append(v2)
        self.edge_count += 1

    def get_vertex_count(self) -> int:
        return self.vertex_count

    def get_edge_count(self) -> int:
        return self.edge_count

    def get_adj(self, v) -> list[int]:
        return self.adj_list[v]

    def get_reverse(self):
        rev_graph = Graph(self.vertex_count)
        for from_node in range(self.vertex_count):
            for to_node in self.adj_list[from_node]:
                rev_graph.add_edge(to_node, from_node)
        return rev_graph

class CycleDetect:
    def __init__(self, g: Graph):
        self.g = g
        self.marked = [False] * self.g.vertex_count
        self.stack = [False] * self.g.vertex_count
        self.has_cycle = False
        for v in range(self.g.vertex_count):
            self.dfs(v)

    def dfs(self, v: int):
        self.stack[v] = True
        self.marked[v] = True
        for adj in self.g.get_adj(v):
            if self.has_cycle:
                return
            if not self.marked[adj]:
                self.dfs(adj)
            else:
                if self.stack[adj]:
                    self.has_cycle = True
                    return
        self.stack[v] = False

    def cycle_detected(self) -> bool:
        return self.has_cycle

class TopologicalSort:
    def __init__(self, g: Graph):
        self.g = g
        self.post_order = []
        self.marked = [False] * g.get_vertex_count()
        for v in range(self.g.vertex_count):
            if not self.marked[v]:
                self.deep_first_order(v)

    def get_order(self):
        return self.post_order[::-1]

    def deep_first_order(self, v: int):
        self.marked[v] = True
        for adj in g.get_adj(v):
            if not self.marked[adj]:
                self.deep_first_order(adj)
        self.post_order.append(v)


g = Graph(6)
g.add_edge(1, 4)
g.add_edge(4, 2)
g.add_edge(1, 3)
g.add_edge(3, 5)
g.add_edge(5, 1)
order = TopologicalSort(g).get_order()
print(order)
print(CycleDetect(g).has_cycle)