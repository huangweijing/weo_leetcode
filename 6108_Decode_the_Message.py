class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        key_map = dict[str, str]()

        for ch in key:
            if not "a" <= ch <= "z":
                continue
            if ch in key_map.keys():
                continue
            # print(ch, chr(ord('a') + len(key_map.keys())))
            key_map[ch] = chr(ord('a') + len(key_map.keys()))
            if len(key_map.keys()) >= 26:
                break

        # print(len(key_map))
        # print(key_map["u"])
        result = ""
        for ch in message:
            if ch not in key_map.keys():
                result += ch
            else:
                result += key_map[ch]

        return result

sol = Solution()
r = sol.decodeMessage("eljuxhpwnyrdgtqkviszcfmabo", "zwx hnfx lqantp mnoeius ycgk vcnjrdb")
print(r)