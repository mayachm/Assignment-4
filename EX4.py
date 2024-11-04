class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node


    def deleteAtLocation(self, position):
     
        if not self.head:
            print("List is empty")
            return

       
        if position == 0:
            self.head = self.head.next
            return

        
        current = self.head
        for _ in range(position - 1):
            if not current.next: 
                print("Position is out of range")
                return
            current = current.next

        if current.next:
            current.next = current.next.next
        else:
            print("Position is out of range")

   
    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(map(str, elements)))


ll = LinkedList()
ll.append(12)
ll.append(56)
ll.append(76)
ll.append(11)
ll.append(0)

print("Original Linked List:")
ll.display()

ll.deleteAtLocation(0)
print("Linked List after deleting node at position 0:")
ll.display()

ll.deleteAtLocation(2)
print("Linked List after deleting node at position 2:")
ll.display()