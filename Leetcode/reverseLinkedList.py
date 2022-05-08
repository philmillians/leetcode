# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        previousNode = None
        currentNode = head
        next = currentNode.next
        while(currentNode):
            next = currentNode.next
            currentNode.next=previousNode
            previousNode = currentNode
            currentNode = next
        return previousNode
