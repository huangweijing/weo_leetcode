from typing import Optional
from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def set_matrix(self, cur: Optional[ListNode], matrix, row, col) -> Optional[ListNode]:
        if cur is None:
            matrix[row][col] = -1
            return None
        else:
            matrix[row][col] = cur.val
            return cur.next

    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[0] * n for m in range(m)]
        direction = 0
        row: int = 0
        col: int = 0
        cur = head
        min_row, max_row, min_col, max_col = 0, m - 1, 0, n - 1
        for i in range(m * n):
            # print(row, col, matrix[row][col], direction)
            # result.append(matrix[row][col])
            cur = self.set_matrix(cur, matrix, row, col)
            if direction == 0:
                if col == max_col:
                    direction = 1
                    min_row += 1
                    row += 1
                else:
                    col += 1
            elif direction == 1:
                if row == max_row:
                    direction = 2
                    max_col -= 1
                    col -= 1
                else:
                    row += 1
            elif direction == 2:
                if col == min_col:
                    direction = 3
                    max_row -= 1
                    row -= 1
                else:
                    col -= 1
            elif direction == 3:
                if row == min_row:
                    direction = 0
                    min_col += 1
                    col += 1
                else:
                    row -= 1
        return matrix


def print_linked_list(head: ListNode, txt=""):
    print(f"{txt} ", end="")
    while head is not None:
        print(head.val, end="" if head.next is None else " > ")
        head = head.next
    print()

def make_link_list(data: list[int]) -> ListNode:
    head: ListNode = None
    last_node: ListNode = None
    for e in data:
        node = ListNode(e, None)
        if head is None:
            head = node
        if last_node is not None:
            last_node.next = node
        last_node = node
    return head

ll = make_link_list([0,1,2])
sol = Solution()
r = sol.spiralMatrix(1, 4, ll)
print(r)