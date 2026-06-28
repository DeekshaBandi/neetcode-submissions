# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nodes = []
        current = head

        while current:
            nodes.append(current)
            current = current.next

        first = 0
        last = len(nodes) - 1

        while first < last:
            nodes[first].next = nodes[last]
            first += 1
            if first >= last:
                break
            nodes[last].next = nodes[first]
            last -= 1

        nodes[first].next = None