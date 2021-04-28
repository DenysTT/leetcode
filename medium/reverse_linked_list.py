class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node
    
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        n = self.head
        while n.next is not None:
            n= n.next
        n.next = new_node
    
    def reverseList(self, head):
        current = head #2
        prev = None
        while current: 
            temp = current.next #3
            current.next = prev # 1
            prev = current #2
            current = temp #3    
        return head




if __name__ == '__main__':

    ll = LinkedList()
    ll.insert_at_end(2)
    ll.insert_at_end(4)
    ll.insert_at_end(3)
    ll2 =  LinkedList()
    ll2.insert_at_end(5)
    ll2.insert_at_end(6)
    ll2.insert_at_end(4)
    addTwoNumbers(ll.head,ll2.head)