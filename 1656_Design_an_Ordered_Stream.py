from typing import List


class OrderedStream:

    def __init__(self, n: int):
        self.sd = dict[int, str]()
        self.n = n
        self.max_chunk_id = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        self.sd[idKey] = value
        ret = []
        for i in range(self.max_chunk_id + 1, len(self.sd) + 1):
            if i in self.sd:
                ret.append(self.sd[i])
                self.max_chunk_id = i
            else:
                break
        return ret


