# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        if not head or not head.next:
            return head
        dummy = ListNode(-float('inf'))
        dummy.next = head
        cur = head
        while cur and cur.next:
            if cur.next.val >= cur.val:
                cur = cur.next
            else:
                tmp = cur.next
                cur.next = tmp.next
                pre = dummy
                while pre.next.val < tmp.val:
                    pre = pre.next
                tmp.next = pre.next
                pre.next = tmp
        return dummy.next
