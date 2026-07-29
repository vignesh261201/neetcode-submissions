# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(head):
            prev = None
            curr = head

            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt    
            return prev

            
        if not head or k == 1:
            return head
        
        dummy = ListNode()
        prev = dummy
        curr = head
        count = 0

        while curr:
            count+=1

            if count == k:
                group_start = head
                next_group = curr.next
                curr.next = None
                
                prev.next  = reverse(group_start)

                head = next_group
                curr = next_group
                prev = group_start
                count = 0
                
            else:
                curr = curr.next
        
        if head:
            prev.next = head

        return dummy.next

            
            
            


            
        