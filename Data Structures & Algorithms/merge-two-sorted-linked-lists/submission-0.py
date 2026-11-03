# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    
        l1 = []
        l2 = []

        while list1 is not None:

            l1.append(list1.val)
            list1 = list1.next

        while list2 is not None:
            l2.append(list2.val)
            list2 = list2.next

        bigList = sorted(l1 + l2)
        newLinked = ListNode()
        current = newLinked

        for val in bigList:
            current.next = ListNode(val)
            current = current.next

        return newLinked.next