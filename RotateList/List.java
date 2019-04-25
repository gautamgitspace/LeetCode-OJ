/*
Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example:
Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL
*/

import java.util.Scanner;
import java.util.*;


class Node {
    public int data;
    public Node next;

    public Node() {
        data = 0;
    }

    public Node(int d, Node n) {
        data = d;
        next = n;
    }

    public void setLink(Node n) {
        next = n;
    }

    public void setData(int d) {
        data = d;
    }

    public Node getLink() {
        return next;
    }

    public int getData() {
        return data;
    }
}

class LinkedList {

    protected Node start;
    protected Node end ;
    public int size ;

    public LinkedList() {
        start = null;
        end = null;
        size = 0;
    }

    public boolean isEmpty() {
        //returns true if start is null
        return start == null;
    }

    public int getSize() {
        return size;
    }

    public void insertAtStart(int data) {
        Node nptr = new Node(data, null);
        size++ ;
        if(start == null)
        {
            start = nptr;
            end = start;
        }
        else
        {
            nptr.setLink(start);
            start = nptr;
        }
    }

    public void display() {
        System.out.print("\nSingly Linked List = ");
        if (size == 0)
        {
            System.out.print("empty\n");
            return;
        }
        if (start.getLink() == null)
        {
            System.out.println(start.getData() );
            return;
        }
        Node ptr = start;
        System.out.print(start.getData()+ "->");
        ptr = start.getLink();
        while (ptr.getLink() != null)
        {
            System.out.print(ptr.getData()+ "->");
            ptr = ptr.getLink();
        }
        System.out.print(ptr.getData()+ "\n");
    }

    public Node rotateList(Node l1, int k) {
      Node prev = new Node();
      Node temp = new Node();
      Node head = l1;
      for (int i = 0; i < k; i++) {
        while (head.next != null) {
          prev = head;
          head = head.next;
        }
        //System.out.println("[DEBUG] prev: " + prev.data);
        //System.out.println("[DEBUG] to_be_swapped: " + head.data);
        //now l1 has the last element and prev has one before it.
        temp = head;
        prev.next = null;

        Node nptr = new Node(temp.data, null);
        size++ ;
        if(start == null) {
            start = head = nptr;
            end = start;
        } else {
            nptr.setLink(start);
            start = head = nptr;
        }
      }
      return start;
    }
    /*  For large values of slow, the usual delete at end and insert at
     *  beginning will be time consuming. The idea is to think of list
     *  as a circle. Basically we need to put elements after len-k%len
     *  to the beginning.
     *  Say if array = {1,2,3}, k=2, move the list after
     *  3-2%1 th node. i.e. 1st node => 3,1,2 and 2,3,1. so we move
     *  2,3 which is after 1st node to the begninning
     */
    public Node rotateListModulas(Node l1, int k) {
      if ((l1 == null) || (l1.next == null))
        return l1;
      Node copyHead = l1;
      int len = 1;
      // compute the length first.
      while (copyHead.next != null) {
        copyHead = copyHead.next;
        len++;
      }
      // now make it circular
      copyHead.next = l1;
      //now keep moving head until len-k%len instances
      //basically we are finding the pivot element here
      for (int i = len - k % len; i > 1; i--) {
        l1 = l1.next;
      }
      // now cut the list again
      copyHead = l1.next;
      l1.next = null;

      return copyHead;
    }
  }


  public class List {
    public static void main(String[] args) {

      LinkedList list1= new LinkedList();
      LinkedList list2 = new LinkedList();
      LinkedList mergedList = new LinkedList();

      Node resultHead = new Node();

      // list1.insertAtStart(5);
      // list1.insertAtStart(4);
      list1.insertAtStart(3);
      list1.insertAtStart(2);
      list1.insertAtStart(1);

      list1.display();
      resultHead = list1.rotateListModulas(list1.start, 1);
      while (resultHead != null) {
        System.out.println(resultHead.data);
        resultHead = resultHead.getLink();
      }

    }
  }
