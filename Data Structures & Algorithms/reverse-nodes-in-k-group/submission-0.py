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

            
        if not head:
            return None
        
        dummy = ListNode()
        prev = dummy
        curr = head

        count = 0
        reversed_linked_list= None

        while curr:
            count+=1

            if count == k:
                temp_head = head
                head = curr.next
                curr.next = None
                curr = head
                count = 0
                reversed_linked_list = reverse(temp_head)
            else:
                curr = curr.next
            
            if reversed_linked_list:
                prev.next = reversed_linked_list
                for i in range(0,k):
                    prev = prev.next
                reversed_linked_list = None

        if head:
            prev.next = head

        return dummy.next

            
            
            


            
        