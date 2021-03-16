class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def add_two_numbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        output: ListNode = ListNode()
        current: ListNode = output
        carry: int = 0

        while l1 or l2:
            value: int = 0

            if l1:
                value = l1.val
                l1 = l1.next
            else:
                l1 = None

            if l2:
                value = value + l2.val
                l2 = l2.next
            else:
                l2 = None

            value = value + carry
            carry = value // 10
            value = value % 10
            current.next = ListNode(value, None)
            current = current.next

        return output.next
