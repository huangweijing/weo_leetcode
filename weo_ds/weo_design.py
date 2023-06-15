class SnapshotArray:
    def __init__(self, length: int):
        pass

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