# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head:
            return head
        
        length = 1
        dummy = head

        while dummy.next:
            dummy = dummy.next
            length += 1
        
        position = k % length
        if position == 0:
            return head
        
        current = head

        for _ in range(length - position - 1):
            current = current.next
        
        new_head = current.next
        current.next = None
        dummy.next = head

        return new_head
# or in cpp
# class Solution {
# public:
#     ListNode* rotateRight(ListNode* head, int k) {
#         if (!head) return head;

#         int length = 1;
#         ListNode* dummy = head;

#         while (dummy->next) {
#             dummy = dummy->next;
#             length++;
#         }

#         int position = k % length;
#         if (position == 0) return head;

#         ListNode* current = head;
#         for (int i = 0; i < length - position - 1; ++i) {
#             current = current->next;
#         }

#         ListNode* newHead = current->next;
#         current->next = nullptr;
#         dummy->next = head;

#         return newHead;        
#     }
# };
