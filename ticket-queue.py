import time
import random

class Queue:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    # Created function simulating selling tickets to a line of people.
    # Accepts two parameters till_show & max_time.
    def simulate_line(self, till_show, max_time):
        # empty queue & empty list to fill
        pq = Queue()
        tix_sold = []

        # Indicating number of people buying tickets from 0-9
        for i in range(10):
            pq.enqueue("person" + str(i))

        # Finds the result of time function plus number of seconds pass to till_show. Creating points in the future.
        t_end = time.time() + till_show
        now = time.time()
        while now < t_end and not pq.is_empty():
            now = time.time()
            r = random.randint(0, max_time)
            time.sleep(r)
            person = pq.dequeue()
            print(person)
            tix_sold.append(person)

        return tix_sold

queue = Queue()
sold = queue.simulate_line(5, 1)
print(sold)
