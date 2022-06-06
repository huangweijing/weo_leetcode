class TextEditor:

    def __init__(self):
        self.text = ""
        self.cur_idx = 0

    def addText(self, text: str) -> None:
        # print(f"addText({text})")
        if self.cur_idx == 0:
            self.text = text + self.text
        elif self.cur_idx == len(self.text):
            self.text = self.text + text
        else:
            self.text = self.text[:self.cur_idx] + text + self.text[self.cur_idx:]
        self.cur_idx += len(text)
        # print(f"text = {self.text}, cursor={self.cur_idx}")

    def deleteText(self, k: int) -> int:
        # print(f"deleteText({k})")
        if k > self.cur_idx:
            k = self.cur_idx
        self.text = self.text[:self.cur_idx - k] + self.text[self.cur_idx:]
        self.cur_idx -= k
        # print(f"text = {self.text}, cursor={self.cur_idx}")
        return k

    def cursorLeft(self, k: int) -> str:
        # print(f"cursorLeft({k})")
        if k > self.cur_idx:
            k = self.cur_idx
        self.cur_idx -= k
        # print(f"text = {self.text}, cursor={self.cur_idx}")
        if self.cur_idx >= 10:
            return self.text[self.cur_idx - 10: self.cur_idx]
        else:
            return self.text[: self.cur_idx]

    def cursorRight(self, k: int) -> str:
        # print(f"cursorRight({k})")
        if k + self.cur_idx >= len(self.text):
            k = len(self.text) - self.cur_idx
        self.cur_idx += k
        # print(f"text = {self.text}, cursor={self.cur_idx}")
        if self.cur_idx >= 10:
            return self.text[self.cur_idx - 10: self.cur_idx]
        else:
            return self.text[: self.cur_idx]

# print("abc"[:0])

sol = TextEditor()
print(sol.cursorRight(*[10]))
print(sol.cursorLeft(*[13]))
print(sol.deleteText(*[4]))
print(sol.addText(*["paszzgqpuxaytw"]))
print(sol.cursorLeft(*[19]))
print(sol.addText(*["rvwidqi"]))
print(sol.cursorRight(*[12]))
print(sol.addText(*["cffnbmmkedhqvfyul"]))
print(sol.cursorLeft(*[14]))
print(sol.cursorRight(*[15]))
print(sol.addText(*["rmlvavjbprfwe"]))
print(sol.cursorLeft(*[7]))
print(sol.deleteText(*[13]))
print(sol.addText(*["e"]))
print(sol.addText(*["sjkrimqbsrwxnnzghzul"]))
print(sol.addText(*["awhrlh"]))
print(sol.deleteText(*[5]))
print(sol.cursorLeft(*[18]))
print(sol.cursorRight(*[11]))
print(sol.addText(*["jxbsaz"]))
print(sol.text + " ****************")
print(str(sol.cur_idx) + " ****************")
print(sol.cursorRight(*[11]))
print(sol.cursorLeft(*[8]))
print(sol.addText(*["pczvvpkxr"]))
print(sol.deleteText(*[10]))
print(sol.addText(*["kwojkaokqffrumzxysl"]))
print(sol.cursorLeft(*[6]))
print(sol.deleteText(*[12]))
print(sol.addText(*["sikivhmnvnfs"]))



# sol.addText("leetcode")
# sol.deleteText(4)
# sol.addText("practice")
# print(sol.cursorRight(3))
# print(sol.cursorLeft(8))
# print(sol.deleteText(10))
# print(sol.cursorLeft(2))
# print(sol.cursorRight(6))
# print(sol.text)
#
# print(*[1, 2, 3])