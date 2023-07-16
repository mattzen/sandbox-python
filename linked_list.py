
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
    
    def hasCyclePointers(self, head: Optional[ListNode]) -> bool:

        return False
    
    
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
  
    
sol = SolutionLinkedList()
sol.hasCycle(n)
    

            