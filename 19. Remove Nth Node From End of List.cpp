'''
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.
'''
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* slow = new ListNode(0);
        slow->next = head;
        ListNode* fast = head;
        if(head->next == NULL){
            return NULL;
        }
        for(int i=0;i<n;i++){
            fast = fast->next;
        }
        cout<<"Fast : "<<fast;
        if(fast == NULL){
            // cout<<"Inside";
            *slow->next = *slow->next->next;
            // cout<<endl<<slow->val<<endl;
        }
        while(fast!=NULL){
            slow = slow->next;
            fast = fast->next;
        }
        // cout<<"Slow : "<<slow->val;
        slow->next = slow->next->next;
        // if(slow->next!=NULL)
        // {
        //     cout<<"In here";
        //     *slow = *slow->next;
        // }
        // else
        // {
        //     *slow->val = NULL;
        // }
        return head;
    }
};
