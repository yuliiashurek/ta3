import numpy as np
import time


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class SCLL:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.next = self.head

    def insert_beginning(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
                # change the links, because we add new node
            temp.next = new_node
            new_node.next = self.head
            self.head = new_node

    def insert_end(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head

    def insert_mid(self, val, size):
        new_node = Node(val)
        # Checks if the list is empty.
        if self.head is None:
            # If list is empty, both head and tail would point to new node.
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
        else:
            # Store the mid-point of the list
            mid = (size // 2) if (size % 2 == 0) else ((size + 1) // 2)
            # temp will point to head
            temp = self.head
            current = 0
            for i in range(0, mid):
                # Current will point to node previous to temp.
                current = temp
                # Traverse through the list till the middle of the list is reached
                temp = temp.next
                # current will point to new node
            current.next = new_node
            # new node will point to temp
            new_node.next = temp
        size += 1

    def delete_end(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
        last = self.head
        while last.next != self.head:
            last = last.next
        last.next = self.head

    def delete_beginning(self):
        if self.head is not None:
            if self.head.next == self.head:
                self.head = None
            else:
                head = self.head
                while head.next != self.head:
                    head = head.next
                self.head = self.head.next
                head.next = self.head

    def delete_mid(self, size):
        if self.head is None:
            return
        else:
            mid = size // 2
            if self.head != self.tail:
                head = self.head
                current = None
                for i in range(0, mid):
                    current = head
                    head = head.next
                if current is not None:
                    current.next = head.next
                else:
                    self.head = self.tail = head.next
                    self.tail.next = self.head
            else:
                self.head = self.tail = None

    def find_index(self, val_to_find):
        current = self.head
        counter = 0
        while current is not None and current.next != self.head:
            if current.val == val_to_find:
                return counter
            counter += 1
            current = current.next
        return False


def rand_scll(start_point: int, end_point: int, num_of_el_in_scll: int):
    scll = SCLL()
    for _ in range(num_of_el_in_scll):
        random_el = np.random.randint(start_point, end_point)
        scll.insert_end(random_el)
    return scll


def display(self):
    head = self.head
    if head is not None:
        while True:
            print(head, end=" ")
            head = head.next
            if head == self.head:
                break
        print()
    else:
        print("The list is empty.")


num_of_el = 10000
singlyCircularLinkedList = rand_scll(1, 100, num_of_el)
print("\tSingly Linked List")
display(singlyCircularLinkedList)

start = time.time()
#
# print("\tAdding to the middle")
# for _ in range(10000):
#     num = np.random.randint(1, 100)
#     singlyCircularLinkedList.insert_mid(num, num_of_el)
#     num_of_el += 1

# print("\tAdding to the beginning")
# for _ in range(10000):
#     num = np.random.randint(1, 100)
#     singlyCircularLinkedList.insert_beginning(num)
#
# print("\tAdding to the end")
# for _ in range(10000):
#     num = np.random.randint(1, 100)
#     singlyCircularLinkedList.insert_end(num)

# ------------------------------------------------------
#
# print("\tDeleting from the middle")
# for _ in range(1000):
#     singlyCircularLinkedList.delete_mid(num_of_el)
#     num_of_el -= 1

# print("\tDeleting from the beginning")
# for _ in range(1000):
#     singlyCircularLinkedList.delete_beginning()
#
# print("\tDeleting from the end")
# for _ in range(1000):
#     singlyCircularLinkedList.delete_end()

# ------------------------------------------------------

print("\tFind index")
for _ in range(1000):
    num = np.random.randint(101, 200)
    singlyCircularLinkedList.find_index(num)

end = time.time()

print("Execution time of the program is ", end - start)
