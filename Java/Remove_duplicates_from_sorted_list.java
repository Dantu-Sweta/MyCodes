/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        if(head == null || head.next == null)
            return head;
        ListNode prev = head;
        ListNode cur = head.next;
        while(cur != null)
        {
            if(prev.val == cur.val)
                cur = cur.next;
            else
            {
                prev.next = cur;
                prev = cur;
                cur = prev.next; 
            }
        }
        prev.next = null;
        return head;
        
    }
}