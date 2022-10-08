from sortedcontainers import SortedDict
import bisect

class MyCalendarThree:

    def __init__(self):
        self.time_dict = SortedDict()
        self.max_val = 0

    def book(self, start: int, end: int) -> int:
        if start not in self.time_dict:
            self.time_dict[start] = [0, 0]
        if end not in self.time_dict:
            self.time_dict[end] = [0, 0]
        self.time_dict[start] = [self.time_dict[start][0] + 1, self.time_dict[start][1]]
        self.time_dict[end] = [self.time_dict[end][0], self.time_dict[end][1] - 1]
        course_cnt = 0
        for v in self.time_dict.values():
            course_cnt += v[0] + v[1]
            self.max_val = max(self.max_val, course_cnt)
        return self.max_val
        # keys = list(self.time_dict.keys())
        # left = bisect.bisect_left(keys, start)
        # right = bisect.bisect_left(keys, end)
        # idx = left
        # course_cnt = 0
        # while idx <= right:
        #     if keys[idx] == keys[left]:
        #         course_cnt += self.time_dict[keys[idx]][0]
        #     elif keys[idx] == keys[right]:
        #         course_cnt += self.time_dict[keys[idx]][1]
        #     else:
        #         course_cnt += self.time_dict[keys[idx]][0]
        #         course_cnt += self.time_dict[keys[idx]][1]
        #     self.max_val = max(self.max_val, course_cnt)
        #     # print(self.time_dict, result)
        #     idx += 1
        # return self.max_val

obj = MyCalendarThree()
print(obj.book(10,20))
print(obj.book(50,60))
print(obj.book(10,40))
print(obj.book(5,15))
print(obj.book(5,10))
print(obj.book(25,55))

# arr = [1, 2, 3, 4]
# print(bisect.bisect_left(arr, 2.5))