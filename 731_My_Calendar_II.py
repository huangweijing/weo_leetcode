import bisect

class MyCalendarTwo:

    def __init__(self):
        self.book_list1 = list[list[int, int]]()
        self.book_list2 = list[list[int, int]]()

    def my_book(self, interval: list[int], book_list: list[list[int, int]]()):
        idx = bisect.bisect_left(book_list, interval[0])
        if idx - 1 >= 0 and book_list[idx - 1][1] > start:
            return False
        if idx + 1 < len(book_list) and book_list[idx + 1][0] < end:
            return False
        book_list.insert(idx, interval)

    def book(self, start: int, end: int) -> bool:
        b1 = self.my_book([start, end], self.book_list1)
        if not b1:
            b2 = self.my_book([start, end], self.book_list2)
            if not b2:
                return False
        return True

c = MyCalendarTwo()
c.book(50, 100)
c.book(30, 60)

        # idx1 = bisect.bisect_left(self.book_list1, start)
        # idx2 = bisect.bisect_left(self.book_list2, start)
        # if idx1 - 1 >= 0 and self.book_list1[idx1 - 1][1] > start:
        #     return False
        # if idx2 - 1 >= 0 and self.book_list2[idx2 - 1][1] > start:
        #     return False
        # if idx1 + 1 < len(self.book_list1) and self.book_list1[idx1 + 1][0] < end:
        #     return False
        # if idx2 + 1 < len(self.book_list2) and self.book_list2[idx2 + 1][0] < end:
        #     return False


