class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        name_compressed = []
        typed_compressed = []
        for ch in name:
            if len(name_compressed) == 0:
                name_compressed.append([ch, 0])
            if name_compressed[-1][0] == ch:
                name_compressed[-1][1] += 1
            else:
                name_compressed.append([ch, 1])

        for ch in typed:
            if len(typed_compressed) == 0:
                typed_compressed.append([ch, 0])
            if typed_compressed[-1][0] == ch:
                typed_compressed[-1][1] += 1
            else:
                typed_compressed.append([ch, 1])

        if len(name_compressed) != len(typed_compressed):
            return False

        for i in range(len(name_compressed)):
            if name_compressed[i][0] == typed_compressed[i][0]:
                if name_compressed[i][1] > typed_compressed[i][1]:
                    return False
            else:
                return False
        return True

