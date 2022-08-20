import bisect


class MyCalendar:

    def __init__(self):
        self.book_list = list[int]()
        self.book_info = dict[int, int]()

    def book(self, start: int, end: int) -> bool:
        idx = bisect.bisect_right(self.book_list, start)
        if idx >= len(self.book_list):
            if len(self.book_list) == 0 or self.book_info[self.book_list[idx - 1]] <= start:
                self.book_list.append(start)
                self.book_info[start] = end
                return True
            else:
                return False
        if idx == 0:
            if end <= self.book_list[idx]:
                self.book_list.insert(0, start)
                self.book_info[start] = end
                return True
            else:
                return False
        if self.book_list[idx] == start:
            return False
        # print(idx, self.book_list, start, end)
        if self.book_info[self.book_list[idx - 1]] > start\
                or end > self.book_list[idx]:
            return False
        else:
            # print(idx, self.book_list, start, end)
            self.book_list.insert(idx, start)
            self.book_info[start] = end
            return True

    def print(self):
        print(self.book_list)
        print(self.book_info)

def test(opers, data):
    cal = None
    for i, oper in enumerate(opers):
        if oper == "MyCalendar":
            cal = MyCalendar()
        elif oper == "book":
            print(cal.book(* data[i]))
            print(f"start={data[i][0]}, end={data[i][1]}, book_list={cal.book_list}, book_info={cal.book_info}")

test(
["MyCalendar","book","book","book","book","book","book","book","book","book","book"]
, [[],[47,50],[33,41],[39,45],[33,42],[25,32],[26,35],[19,25],[3,8],[8,13],[18,27]]
)
#
# l = [1, 4, 8, 9]
# l.insert(0, 2)
# print(l)