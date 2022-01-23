# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next=head
        
        left, right = dummy, head
        
        while right:
            mynext = right.next
            
            if right.val == val:
                left.next=mynext
            else:
                left = right
            right=right.next
        
        return dummy.next
        


### No dummy Soln ###
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        prev = None
        curNode = head
        while curNode:
            if curNode.val == val and prev:
                prev.next = curNode.next
            elif curNode.val == val and not prev:
                head = curNode.next
            else:
                prev = curNode
            curNode = curNode.next
        return head