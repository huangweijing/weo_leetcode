from sortedcontainers import SortedList


class Space:
    n = 0

    def __init__(self, s: int, e: int) -> None:
        self.s, self.e = s, e
        if self.s == 0:
            self.len = e
        elif self.e == Space.n - 1:
            self.len = Space.n - s - 1
        else:
            self.len = (e - s) // 2
        self.mid = -1

    def occupy(self) -> list:
        if self.s == 0:
            self.mid = 0
            return [Space(1, self.e)]
        elif self.e == Space.n - 1:
            self.mid = self.e
            return [Space(self.s, self.e - 1)]
        else:
            if self.s == self.e:
                self.mid = self.s
                return []
            self.mid = (self.e + self.s) >> 1
            if self.mid == self.s:
                return [Space(self.mid + 1, self.e)]
            else:
                return [Space(self.s, self.mid - 1), Space(self.mid + 1, self.e)]

    def __lt__(self, other):
        if self.len == other.len:
            return self.s < other.s
        else:
            return self.len > other.len

    def __str__(self):
        return f"<Space s={self.s}, e={self.e}, len={self.len}>"


class ExamRoom:

    def __init__(self, n: int):
        Space.n = n
        self.n = n
        self.space_list = SortedList()
        self.s_dict = dict[int, Space]()
        self.e_dict = dict[int, Space]()
        space = Space(0, n - 1)
        self.space_list.add(space)
        self.s_dict[space.s] = space
        self.e_dict[space.e] = space

    def seat(self) -> int:
        space = self.space_list[0]
        self.space_list.remove(space)
        new_space_list = space.occupy()
        del self.s_dict[space.s]
        del self.e_dict[space.e]
        for new_space in new_space_list:
            self.s_dict[new_space.s] = new_space
            self.e_dict[new_space.e] = new_space
            self.space_list.add(new_space)
        return space.mid

    def leave(self, p: int) -> None:
        if p + 1 in self.s_dict:
            s1 = self.s_dict[p + 1]
            del self.s_dict[s1.s]
            del self.e_dict[s1.e]
            self.space_list.remove(s1)
        else:
            s1 = None
        if p - 1 in self.e_dict:
            s2 = self.e_dict[p - 1]
            del self.s_dict[s2.s]
            del self.e_dict[s2.e]
            self.space_list.remove(s2)
        else:
            s2 = None
        # print("aaaa", s1, s2, [[k, str(v)] for k, v in self.e_dict.items()])
        if s1 is None and s2 is None:
            new_space = Space(p, p)
        elif s1 is None:
            new_space = Space(s2.s, p)
        elif s2 is None:
            new_space = Space(p, s1.e)
        else:
            new_space = Space(s2.s, s1.e)

        self.s_dict[new_space.s] = new_space
        self.e_dict[new_space.e] = new_space
        self.space_list.add(new_space)


data = [
    ["ExamRoom", "seat", "seat", "seat", "leave", "leave", "seat", "seat", "seat", "seat", "seat", "seat", "seat",
     "seat", "seat", "leave"]
    , [[10], [], [], [], [0], [4], [], [], [], [], [], [], [], [], [], [0]]
]
ssa = ExamRoom(*data[1][0])
result = []
for idx, command in enumerate(zip(data[0], data[1])):
    if idx == 0:
        continue
    ret = getattr(ssa, command[0])(* command[1])
    print(command[0], command[1], ret, list(map(str, ssa.space_list)), ssa.s_dict.keys(), ssa.e_dict.keys())
    result.append(ret)
print(result)