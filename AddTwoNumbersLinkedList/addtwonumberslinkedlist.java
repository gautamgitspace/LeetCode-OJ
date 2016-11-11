/**
 * LEETCODE OJ Problem 2
 * Created by Gautam on 6/3/16.
 * CTCI 2.5a - Add contents of two lists and return the sum in a resultant list. The digits are stored in the reverse order.
 */
public class CTCI2_5
{
    static Node head1, head2;

        static class Node
        {
            int data;
            Node next;
            Node(int d)
            {
                data = d;
                next = null;
            }
        }

        /* Adds contents of two linked lists and return the head node of resultant list */
        Node addTwoLists(Node first, Node second)
        {
            Node resultantHead = null;
            Node prev = null;
            Node temp = null;
            int carry = 0, sum;

            /*MAIN LOOP TO ITERATE THROUGH THE LIST*/
            while (first != null || second != null)
            {
                sum = carry + (first != null ? first.data : 0) + (second != null ? second.data : 0);
                System.out.println("sum is: " + sum);

                //if sum is greater than 10 then carry 1 else carry 0
                carry = (sum >= 10) ? 1 : 0;
                System.out.println("carry is: " + carry);

                //if sum is greater than 10, base part gets updated
                sum = sum % 10;

                temp = new Node(sum);

                if (resultantHead == null)
                {
                    //case when this is the only node in the resultant sum list
                    resultantHead = temp;
                }
                else
                {
                    //case when other nodes exist, add it to existing
                    prev.next = temp;
                }

                /*keep track of prev for the resultant list*/
                prev = temp;

                /*ITERATORS FOR WHILE LOOP - keep moving first and second until they reach null*/
                if (first != null)
                {
                    first = first.next;
                }
                if (second != null)
                {
                    second = second.next;
                }
            }

            if (carry > 0)
            {
                /*last carry case. create a new node and add it to the end of the resultant list*/
                temp.next = new Node(carry);
                System.out.println("Last carry case");
            }

            // return head of the resultant list
            return resultantHead;
        }

        private void printList(Node head)
        {
            while (head != null)
            {
                System.out.print(head.data + "->");
                head = head.next;
            }
            if(head==null)
            {
                System.out.println("null");
            }
            System.out.println("");
        }

        public static void main(String[] args)
        {
            CTCI2_5 list = new CTCI2_5();

            //create list head1
            list.head1 = new Node(1);
            list.head1.next = new Node(2);
            list.head1.next.next = new Node(3);
            list.head1.next.next.next = new Node(4);
            //list.head1.next.next.next.next = new Node(9);
            System.out.print("First List is ");
            list.printList(head1);

            //create list head2
            list.head2 = new Node(5);
            list.head2.next = new Node(6);
            list.head2.next.next = new Node(7);
            //list.head2.next.next.next = new Node(8);
            System.out.print("Second List is ");
            list.printList(head2);

            //call to addTwoLists function
            Node result = list.addTwoLists(head1, head2);
            System.out.print("Resultant List is ");
            list.printList(result);
        }
    }
