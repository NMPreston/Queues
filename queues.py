# Noah Preston , CSC-231-001

from doubly_linked_list import DoublyLinkedList

class QueuePythonList:
    def __init__(self):
        self.items = []  # Create list

    def enqueue(self, item): # Add item 
        self.items.append(item)

    def dequeue(self): # Remove and return item 
        if self.is_empty():
            return None
        return self.items.pop(0)  

    def is_empty(self): # Check if queue is empty
        return len(self.items) == 0

    def __len__(self): # Return number of items
        return len(self.items)


class QueueLinkedList:
    def __init__(self):
        self.list = DoublyLinkedList()  

    def enqueue(self, item): # Add an item 
        self.list.append(item)  

    def dequeue(self): # Remove and return item 
        if self.is_empty():
            return None
        return self.list.pop(0)  

    def is_empty(self): # Check if queue is empty
        return self.list.is_empty()

    def __len__(self): # Return number of items 
        return len(self.list)

if __name__ == '__main__':
    # You may add code below this line to help you test.

    # You may comment out the calls to the test_xxx() functions to reduce the amount printed to the screen as you work.
    # Uncomment them when you are ready to test.

    from queue_tests import QueueTests
    import sys

    print("===== Testing QueuePythonList =====")
    suite = QueueTests(sys.modules[__name__], "QueuePythonList")
    suite.test_01_constructor()
    suite.test_02_enqueue_dequeue()
    suite.test_03_dequeue_empty()
    suite.test_04_is_empty()
    suite.test_05__len__()

    print("\n===== Testing QueueLinkedList =====")
    suite = QueueTests(sys.modules[__name__], "QueueLinkedList")
    suite.test_01_constructor()
    suite.test_02_enqueue_dequeue()
    suite.test_03_dequeue_empty()
    suite.test_04_is_empty()
    suite.test_05__len__()
