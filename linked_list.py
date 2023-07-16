
from typing import *

class ListNode:
     def __init__(self, x):
        self.val = x
        self.next = None

class SolutionLinkedList:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        while(head):
            if(head in visited):
                return True
            visited.add(head)
            head = head.next
        return False
    
    def hasCycleFloyd(self, head: Optional[ListNode]) -> bool:
        slow_p = head
        fast_p = head
        while(slow_p and fast_p and fast_p.next):
            slow_p = slow_p.next
            fast_p = fast_p.next.next
            if slow_p == fast_p:
                return 1
        return 0
    
    
    def printLinkedList(self, head: Optional[ListNode]):
        while(head):
            print(head.val)
            head = head.next
    
    
#[3,2,0,-4]
n = ListNode(3)
n.next = ListNode(2)
n.next.next = ListNode(0)
n.next.next.next = ListNode(-4)
n.next.next.next.next = n.next
  
n1 = ListNode(1)

sol = SolutionLinkedList()
if(sol.hasCyclePointers(n)):
    print("Loop Found")
else:
    print("No Loop")
    

            