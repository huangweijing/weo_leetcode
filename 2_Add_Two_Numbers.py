# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def fromDigit(val:int):
    num = val
    firstNode = ListNode()
    firstNode.next = None
    firstNode.val = num % 10
    num = int(num / 10)
    lastNode = firstNode

    while num != 0:
        oneDigit = num % 10
        num = int(num / 10)
        currentNode = ListNode()
        currentNode.val = oneDigit
        lastNode.next = currentNode
        lastNode = currentNode
    return firstNode

def printList(firstNode : ListNode):
    currentNode = firstNode
    while currentNode != None:
        print(str(currentNode.val) + "->", end="")
        currentNode = currentNode.next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1CurrentNode = l1
        l2CurrentNode = l2
        l3 = ListNode(0, None)
        l3CurrentNode = l3
        stepUp = 0
        l3LastNode = None
        while l1CurrentNode is not None or l2CurrentNode is not None:

            if l1CurrentNode is not None:
                val1 = l1CurrentNode.val
            else:
                val1 = 0
            if l2CurrentNode is not None:
                val2 = l2CurrentNode.val
            else:
                val2 = 0

            sum = val1 + val2 + stepUp
            print(sum)
            l3CurrentNode.val = sum % 10
            # 进位处理
            if sum >= 10:
                stepUp = 1
            else:
                stepUp = 0

            if l3LastNode is not None:
                l3LastNode.next = l3CurrentNode
            l3LastNode = l3CurrentNode
            l3CurrentNode = ListNode(0, None)

            if l1CurrentNode is not None:
                l1CurrentNode = l1CurrentNode.next
            if l2CurrentNode is not None:
                l2CurrentNode = l2CurrentNode.next

        if stepUp == 1:
            l3CurrentNode = ListNode(1, None)
            l3LastNode.next = l3CurrentNode

        return l3

num1 = fromDigit(9999999)
num2 = fromDigit(   9999)
sol = Solution()
num3 = sol.addTwoNumbers(num1, num2)
# print(firstNode.)
printList(num3)
# print()
# printList(num2)