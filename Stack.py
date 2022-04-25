class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def isempty(self):
        if self.head is None:
            return True
        else:
            return False

    # додає перший елемент (head)
    def push(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

    # видаляє перший елемент
    def pop(self):
        if self.isempty():
            return None
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            return temp.data

    # повертає перший елемент
    def peek(self):
        if self.isempty():
            return None
        else:
            return self.head.data

    def display(self):
        temp = self.head
        if self.isempty():
            print("stack is empty")
        else:
            while temp is not None:
                print(temp.data, end=" ")
                temp = temp.next
            return


stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)

stack.display()

print("\nTop element is ", stack.peek())

stack.pop()
stack.pop()

stack.display()
