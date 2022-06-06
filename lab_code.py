bbb = "abcdadf"

def m(t:str):
    for i in t:
        print(t.count(i))
        if t.count(i) == 1:
            return i
        else:
            return "no"
print(m(bbb))