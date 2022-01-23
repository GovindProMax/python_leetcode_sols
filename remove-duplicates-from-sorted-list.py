class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next=head
        mydict={}
        
        left, right = dummy, head
        
        while right:
            mynext = right.next
            
            if right.val in mydict:
                left.next=mynext
            else:
                mydict[right.val] = 0
                left = right
            right=right.next
        
        print(mydict)
        
        return dummy.next