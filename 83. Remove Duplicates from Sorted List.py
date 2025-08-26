
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = head

        while head and head.next:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next
        
        return res
# in cpp
# class Solution {
# public:
#     ListNode* deleteDuplicates(ListNode* head) {
#         ListNode* res = head;

#         while (head && head->next) {
#             if (head->val == head->next->val) {
#                 head->next = head->next->next;
#             } else {
#                 head = head->next;
#             }
#         }

#         return res;        
#     }
# };

# in java 
# class Solution {
#     public ListNode deleteDuplicates(ListNode head) {
#         ListNode res = head;

#         while (head != null && head.next != null) {
#             if (head.val == head.next.val) {
#                 head.next = head.next.next;
#             } else {
#                 head = head.next;
#             }
#         }

#         return res;        
#     }
# }
