### Meh Solution ###
def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr=[]
        while head.next:
            arr.append(head.val)
            head=head.next
        arr.append(head.val) 
        
        return arr == arr[::-1]




### O(1) Soln ###
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast=head
        slow=head
        
        while fast and fast.next:
            fast = fast.next.next
            slow=slow.next
        
        prev,curr=None,slow
    
        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
    
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True