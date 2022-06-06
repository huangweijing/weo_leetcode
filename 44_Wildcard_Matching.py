class UndirectedGraph():
    def __init__(self, vertex_count: int):
        self.vertex_adj_list = [[] for x in range(vertex_count)]
        self.edge_count = 0
        self.vertex_count = vertex_count

    def add_edge(self, v1: int, v2: int):
        self.vertex_adj_list[v1].append(v2)
        self.edge_count += 1

    def get_vertex_count(self) -> int:
        return self.vertex_count

    def get_edge_count(self) -> int:
        return self.edge_count

    def get_adjacent_vertex(self, v) -> list[int]:
        return self.vertex_adj_list[v]

    def print_graph(self):
        for i in range(self.vertex_count):
            print(f"{i} -> {self.vertex_adj_list[i]}")

class WeoRegular:
    def __init__(self, re: str):
        re = "S" + re + "E"
        self.re = re
        self.g = UndirectedGraph(len(re))
        for idx in range(len(re) - 1):
            self.g.add_edge(idx, idx + 1)
            if re[idx] == "*":
                self.g.add_edge(idx, idx)

            # skip wildcard *
            look_forward = idx + 1
            while look_forward + 1 < len(re) and re[look_forward] == "*":
                look_forward += 1
            self.g.add_edge(idx, look_forward)


            # if idx + 2 < len(re) and re[idx + 1] in ["*"]:
            #     self.g.add_edge(idx, idx + 2)

    def expand_state(self, step_list: set[int]) -> set[int]:
        new_step_list = set[int]()
        expanded = False
        for step in step_list:
            if self.re[step] == "S":
                for adj in self.g.get_adjacent_vertex(step):
                    new_step_list.add(adj)
                    expanded = True
            else:
                new_step_list.add(step)
        if expanded:
            return self.expand_state(new_step_list)
        return new_step_list

    def dg_nfs(self, step_list: list[str]) -> set[int]:
        # self.g.print_graph()
        available_state = set[int]()
        available_state.add(0)
        available_state = self.expand_state(available_state)
        for step in step_list:
            new_available_state = set[int]()
            for state in available_state:
                if self.re[state] == step or self.re[state] in ["?", "*"]:
                    for adj in self.g.get_adjacent_vertex(state):
                        new_available_state.add(adj)

            # new_available_state = self.expand_state(new_available_state)

            # print(f"step_list={step_list}, step={step}, re={self.re}"
            #       f", available_state={available_state}, new_available_state={new_available_state}")
            available_state = new_available_state
            # if len(available_state) == 0:
            #     return None
        return available_state

    def is_match(self, s: str):
        end_states = self.dg_nfs([ch for ch in s])
        if end_states is not None and self.g.vertex_count - 1 in end_states:
            return True
        else:
            return False


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        weo_re = WeoRegular(p)
        return weo_re.is_match(s)

weo_re = WeoRegular("****")
r = weo_re.is_match("")
print(r)

# g = UndirectedGraph(vertex_count=10)
# g.set_data([ch for ch in "abcdefghij"])
# g.add_edge(0, 1)
# g.add_edge(0, 2)
# g.add_edge(2, 2)
# g.add_edge(2, 1)
# g.add_edge(1, 4)
# g.add_edge(2, 7)
# g.add_edge(7, 8)
# g.add_edge(8, 9)
# g.add_edge(4, 9)
# r = g.dg_nfs([ch for ch in "acccc"])
# print(r)

# sol = Solution()
# r = sol.isMatch("aaab", "a*aaaab")
# print(r)

