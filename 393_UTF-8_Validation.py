from typing import List

class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        # print(list(map(bin, data)))
        template = [0b00000000, 0b11000000, 0b11100000, 0b11110000]
        mask_arr = [0b10000000, 0b11100000, 0b11110000, 0b11111000]
        byte_idx = 0
        mask_type = 0
        while byte_idx < len(data):
            byte = data[byte_idx]
            mask_type = -1
            for i, mask in enumerate(mask_arr):
                # print(bin(byte), bin(mask))
                if mask_arr[i] & byte == template[i]:
                    mask_type = i
                    # print(byte, bin(byte), bin(mask), i, bin(mask & byte))
                    break
            # print(mask_type)
            if not 0 <= mask_type <= 3:
                return False
            while mask_type > 0 and byte_idx < len(data):
                byte_idx += 1
                if byte_idx >= len(data):
                    return False
                byte = data[byte_idx]
                if 0b11000000 & byte != 0b10000000:
                    return False
                # print(bin(byte))
                mask_type -= 1
            byte_idx += 1

        if mask_type != 0:
            return False
        return True


data = [1]
r = Solution().validUtf8(data)
print(r)