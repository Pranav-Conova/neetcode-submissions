# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        result = None
        if current:
            result = ListNode(current.val)
        if current and current.next:
            current = current.next
            while current:
                new_node = ListNode(current.val, result)
                result = new_node
                current = current.next
        return result

