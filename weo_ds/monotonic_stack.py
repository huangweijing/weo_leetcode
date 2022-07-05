class MonotonicStack:
    def __init__(self):
        pass

    def left_gt_arr(self, data: list[int]) -> list[int]:
        result: list[int] = []
        mon_stack: list[int] = []
        for i in range(len(data)):
            while len(mon_stack) > 0 and mon_stack[-1] < data[i]:
                mon_stack.pop()
            if len(mon_stack) == 0:
                result.append(-1)
            else:
                result.append(mon_stack[-1])
            mon_stack.append(data[i])
        return result

    def right_gt_arr(self, data: list[int]) -> list[int]:
        result: list[int] = []
        mon_stack: list[int] = []
        for i in range(len(data) - 1, -1, -1):
            while len(mon_stack) > 0 and mon_stack[-1] < data[i]:
                mon_stack.pop()
            # print(i, data, mon_stack)
            if len(mon_stack) == 0:
                result.append(-1)
            else:
                result.append(mon_stack[-1])
            mon_stack.append(data[i])
        result.reverse()
        return result

r = MonotonicStack().left_gt_arr([7, 2, 3, 2, 2, 7])
print(r)
r = MonotonicStack().right_gt_arr([7, 2, 3, 2, 2, 7])
print(r)