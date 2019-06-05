"""
This module is implementation of Linked List data structure in python.
Python version support is 3.7

"""

class ListNode:
    """
    A Node in singly LinkedList
    """
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return repr(f'Data:{self.data} Next:{type(self.next)}')


class SinglyLinkedList:
    """
    This class is implementation of singly linked list
    """
    def ___init__(self):
        """
        Create a new singly linked list takes O(1) time
        """
        self.head = None

    def __repr__(self):
        """
        Return a string representation of list
        takes O(n) time
        :return:
        """
        temp = self.head
        ss = []
        while True:
            ss.append(temp.data)
            if not temp.next:
                return repr('-->'.join([str(i) for i in ss]))
            temp = temp.next

    def prepend(self, data):
        """
        add single node at the beginning of list takes O(1) time
        :param data:
        """
        new_head = ListNode(data)
        new_head.next = self.head
        self.head = new_head

    def append(self, data):
        """
        Insert new element at the end of the list
        takes O(n) time
        :param data:
        :return:
        """
        temp = self.head
        while True:
            if not temp.next:
                break
            temp = temp.next
        new_end_node = ListNode(data)
        temp.next = new_end_node

    def find(self, key):
        """
        Search for first element with data matching key Return the element or None if not found.
        Takes O(n) time
        :param key:
        :return:
        """
        temp = self.head
        while True:
            if temp.data == key:
                return temp
            if not temp.next:
                return
            temp = temp.next

    def remove(self, key):
        """
        Remove the first occurrence of `key` in the list.
        Takes O(n) time.
        :param key:
        :return:
        """

    def reverse_print(self, head):
        if head is None:
            return head
        else:
            self.reverse_print(head.next)
            print(head.data)

    def reverse(self):
        """
        
        :return:
        """
        prev = None
        cur = self.head
        # next1 = None

        while cur:
            next1 = cur.next
            cur.next = prev
            prev = cur
            cur = next1

        self.head = prev


if __name__ == '__main__':
    node1 = ListNode(1)
    list1 = SinglyLinkedList()
    list1.head = node1
    # print(node1)
    # print(list1)
    # print(type(list1.head))
    list1.prepend(0)
    list1.append(2)
    print(list1)
    # print(list1.find(2))
    # list1.reverse_two()
    print(list1)
    list1.reverse_print(list1.head)
