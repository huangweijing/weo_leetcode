class Solution:
    def capitalizeTitle(self, title: str) -> str:
        title = title.lower()
        title_arr = title.split(sep=" ")
        result = list[str]()
        for t in title_arr:
            if len(t) > 2:
                result.append(t[0].upper() + t[1:])
            else:
                result.append(t)

        return " ".join(result)
