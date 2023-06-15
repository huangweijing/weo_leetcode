from collections import defaultdict
import bisect

class SnapshotArray:

    def __init__(self, length: int):
        self.arr = list[list[list[int]]]()
        for i in range(length):
            self.arr.append([
                [0]
                , [0]
            ])
        self.snap_ver = 0

    def set(self, index: int, val: int) -> None:
        snap_idx_list = self.arr[index][0]
        snap_val_list = self.arr[index][1]
        if snap_idx_list[-1] == self.snap_ver:
            snap_val_list[-1] = val
        else:
            snap_idx_list.append(self.snap_ver)
            snap_val_list.append(val)

    def snap(self) -> int:
        snap_ver = self.snap_ver
        self.snap_ver += 1
        return snap_ver

    def get(self, index: int, snap_id: int) -> int:
        snap_idx_list = self.arr[index][0]
        snap_val_list = self.arr[index][1]
        val_idx = bisect.bisect_right(snap_idx_list, snap_id) - 1
        return snap_val_list[val_idx]


data = [
    ["SnapshotArray","set","snap","snap","snap","get","snap","snap","get"]
    , [[1],[0,15],[],[],[],[0,2],[],[],[0,0]]
]
ssa = SnapshotArray(*data[1][0])
result = []
for idx, command in enumerate(zip(data[0], data[1])):
    if idx == 0:
        continue
    ret = getattr(ssa, command[0])(* command[1])
    print(command[0], command[1], ret)
    result.append(ret)
print(result)
