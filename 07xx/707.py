class ListNode():
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

class MyLinkedList(object):
    def __init__(self):
        self.root = None

    def get(self, index):
        if self.root == None:
            return -1
        if index == 0:
            return self.root.value
        node = self.root
        while(index):
            node = node.next
            index -= 1
            if node == None:
                return -1
            if index == 0:
                return node.value
        
    def addAtHead(self, val):
        if self.root == None:
            self.root = ListNode(val)
        else:
            node = ListNode(val, self.root)
            self.root = node        

    def addAtTail(self, val):
        if self.root == None:
            self.root = ListNode(val)
        else:
            node = self.root
            while(node.next != None):
                node = node.next
            node.next = ListNode(val)
        
    def addAtIndex(self, index, val):
        if self.root == None:
            self.root = ListNode(val)
        if index == 0:
            self.root = ListNode(val, self.root)
        node = self.root
        while(index - 1 != 0):
            node = node.next
            index -= 1
            if index != 0 and node == None:
                return
        next = node.next
        node.next = ListNode(val, next)
        
    def deleteAtIndex(self, index):
        if self.root == None:
            return
        if index == 0:
            self.root = self.root.next
            return
        node = self.root
        while(index != 0):
            index -= 1
            if index == 0:
                if node.next == None:
                    return
                node.next = node.next.next
            node = node.next
            if node == None:
                return

    def print_list(self):
        if self.root == None:
            print('empty')
        else:
            node = self.root
            while node != None:
                print(node.value, end=' ')
                node = node.next
            print()

def test3():
    a = MyLinkedList()
    a.addAtHead(4)
    a.print_list()
    a.get(1)
    a.addAtHead(1)

    a.print_list()
    a.addAtHead(5)

    a.print_list()
    a.deleteAtIndex(3)

    a.print_list()
    a.addAtHead(7)

    a.print_list()
    a.get(3)
    a.get(3)
    a.get(3)
    a.addAtHead(1)

    a.print_list()
    a.deleteAtIndex(4)

    a.print_list()


def test2():
    a = MyLinkedList()
    a.print_list()
    print("----")
    a.addAtIndex(0, 10)
    a.print_list()
    print("----")
    a.addAtIndex(0, 20)
    a.print_list()
    print("----")
    a.addAtIndex(1, 30)    
    a.print_list()
    print("----")

    a.get(0)

def test1():
    a = MyLinkedList()
    a.print_list()

    a.addAtHead(1)
    a.print_list()

    a.addAtTail(3)
    a.print_list()

    a.addAtIndex(1, 2)
    a.print_list()

    print('get', a.get(1))
    a.print_list()

    a.deleteAtIndex(0)
    a.print_list()

    print('get', a.get(0))


test1()

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)