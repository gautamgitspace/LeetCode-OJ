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

    public static Node mergeTwoLists(Node l1, Node l2) {
      Node head = new Node();
      Node wrkgNode = head;
      while (l1 != null && l2 != null) {
        if (l1.data > l2.data) {
          wrkgNode.next = l2;
          l2 = l2.next;
        } else {
          wrkgNode.next = l1;
          l1 = l1.next;
        }
        wrkgNode = wrkgNode.next;
      }//while ends

      /* process the last element */
      if (l1 != null) {
        wrkgNode.next = l1;
      }
      if (l2 != null) {
        wrkgNode.next = l2;
      }
      return head.next;
    }
}


public class List {
  public static void main(String[] args) {

    LinkedList list1= new LinkedList();
    LinkedList list2 = new LinkedList();
    LinkedList mergedList = new LinkedList();

    Node resultHead = new Node();

    list1.insertAtStart(11);
    list1.insertAtStart(9);
    list1.insertAtStart(5);
    list1.insertAtStart(1);

    list2.insertAtStart(12);
    list2.insertAtStart(10);
    list2.insertAtStart(7);

    list1.display();
    list2.display();

    resultHead = mergedList.mergeTwoLists(list1.start, list2.start);

    while (resultHead!=null){
      System.out.println(resultHead.data);
      resultHead = resultHead.getLink();
    }
  }
}
