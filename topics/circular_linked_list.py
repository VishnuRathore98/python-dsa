class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head   # points to itself
            return
        current = self.head
        while current.next != self.head:
            current = current.next
        current.next = new_node
        new_node.next = self.head       # close the loop

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return
        current = self.head
        while current.next != self.head:
            current = current.next
        new_node.next = self.head
        current.next = new_node
        self.head = new_node

    def delete(self, data):
        if self.head is None:
            return
        current = self.head
        prev = None

        # deleting the head node
        if current.data == data:
            if current.next == self.head:   # only one node
                self.head = None
                return
            while current.next != self.head:
                current = current.next
            current.next = self.head.next
            self.head = self.head.next
            return

        # deleting a non-head node
        prev = self.head
        current = self.head.next
        while current != self.head:
            if current.data == data:
                prev.next = current.next
                return
            prev = current
            current = current.next

    def print_list(self):
        if self.head is None:
            print("Empty list")
            return
        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print("(back to head)")


cll = CircularLinkedList()
cll.append(10)
cll.append(20)
cll.append(30)
cll.prepend(5)
cll.print_list()    # 5 -> 10 -> 20 -> 30 -> (back to head)

cll.delete(20)
cll.print_list()    # 5 -> 10 -> 30 -> (back to head)
