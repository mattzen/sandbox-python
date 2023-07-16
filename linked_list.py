
from typing import *

class ListNode:
     def __init__(self, x):
        self.val = x
        self.next = None

class SolutionLinkedList:
    def printLinkedList(self, head: Optional[ListNode]):
        while(head):
            print(head.val)
            head = head.next
            
    def hasCycleSet(self, head: Optional[ListNode]) -> bool:
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
    
    def detectLoopTwoPointers(self, head: Optional[ListNode]) -> bool:
    # Create a temporary node
        temp = ""
        while (head != None):
    
            # This condition is for the case
            # when there is no loop
            if (head.next == None):
                return False
    
            # Check if next is already
            # pointing to temp
            if (head.next == temp):
                return True
    
            # Store the pointer to the next node
            # in order to get to it in the next step
            next = head.next
    
            # Make next point to temp
            head.next = temp
    
            # Get to the next node in the list
            head = next
    
        return False
    
#[3,2,0,-4]
n = ListNode(3)
n.next = ListNode(2)
n.next.next = ListNode(0)
n.next.next.next = ListNode(-4)
n.next.next.next.next = n.next
  
n1 = ListNode(1)

sol = SolutionLinkedList()
if(sol.detectLoopTwoPointers(n)):
    print("Loop Found")
else:
    print("No Loop")
    

            