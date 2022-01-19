# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head == None:
            return None
        if head.next == None:
            return head

        
        new_head=head.next
        head.next=None
        
        while new_head.next:
            temp = new_head.next
            new_head.next=head
            head = new_head
            new_head = temp
            
            #print("head is " ,head, "new head is ", new_head, "temp is ", temp, "temp.next is ",temp.next)
        
        new_head.next=head
        return new_head

### Alternate fewer line implementation###
def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

    prev,curr=None,head
    
    while curr:
        nxt=curr.next
        curr.next=prev
        prev=curr
        curr=nxt
    
    return prev