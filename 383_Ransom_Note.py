class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_dict = dict[str, int]()
        mag_dict = dict[str, int]()

        for ch in ransomNote:
            if ch not in ransom_dict:
                ransom_dict[ch] = 0
            ransom_dict[ch] += 1

        for ch in magazine:
            if ch not in mag_dict:
                mag_dict[ch] = 0
            mag_dict[ch] += 1

        for key in ransom_dict:
            if key not in mag_dict:
                return False
            if ransom_dict[key] > mag_dict[key]:
                return False

        return True
