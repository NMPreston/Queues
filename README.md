Queues.py

This project focuses on implementing and testing the Queue Abstract Data Type (ADT) using two different data structures in Python: a Python list and a custom DoublyLinkedList. The code supports key queue operations such as enqueue, dequeue, is_empty, and __len__.

Project Structure

queues.py: The main Python script containing the implementation of the Queue ADT using both a Python list and a DoublyLinkedList.
router.py: An experimental script to test the performance of the different queue implementations under various traffic conditions.
results.xlsx: A spreadsheet where test results from running router.py can be recorded for analysis.
Features

enqueue: Adds an element to the end of the queue.
dequeue: Removes and returns the element at the front of the queue.
is_empty: Checks if the queue is empty.
len: Returns the number of elements in the queue.
How to Use

Running the Queue Implementation:
Ensure Python (version 3.x) is installed on your system.
Run the queues.py file to test individual operations:
python queues.py
Testing with router.py:
Run router.py to simulate traffic conditions and test the performance of the queue implementations.
python router.py
Record the performance metrics in results.xlsx for further analysis.
