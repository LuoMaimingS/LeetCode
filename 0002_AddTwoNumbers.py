# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        empty_head = ListNode(0)
        current_node = empty_head
        while True:
            v1 = l1.val if l1 is not None else 0
            v2 = l2.val if l2 is not None else 0
            temp_sum = v1 + v2 + carry
            if temp_sum >= 10:
                temp_sum -= 10
                carry = 1
            else:
                carry = 0
            temp_node = ListNode(temp_sum)
            current_node.next = temp_node
            current_node = temp_node

            l1 = l1.next if (l1 is not None and l1.next is not None) else None
            l2 = l2.next if (l2 is not None and l2.next is not None) else None

            if l1 is None and l2 is None:
                if carry == 1:
                    temp_node = ListNode(1)
                    current_node.next = temp_node
                break

        return empty_head.next
