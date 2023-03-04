#Queue is a linear data structure and consists of elements which adds and removes elements by FIFO methodology
# Enqueue   Dequeue   isFull    isEmpty (Operations in queue)
#Implementation of queue using lists
# queue = []#Creation of an emoty list
# queue.append(10)
# queue.append(20)   #Element added from the tail of the queue
# queue.append(30)
# queue.append(40)
# print(queue)
# queue.pop(0)   #The 0th index element will be removed
# print(queue)   
# queue.pop(0)
# print(queue)
# queue.pop(0)
# print(queue)
# queue.pop(0)
# print(queue)

#Program for implementation of queues using lists

# queue = []

# def enqueue(element):
#     queue.append(element)
#     print(queue)
# def dequeue():
#     if not queue:
#         print("Queue is empty")
#     else:
#         queue.pop(0)
#         print(queue)


# while True:
#     choice = int(input("Enter 1 for eneueue \n2 for dequeue \n3 for checking the size of the queue\nAny key for quit "))

#     if(choice==1):
#         element=int(input("Enter the element for enqueue"))
#         enqueue(element)
#     elif(choice==2):
#             dequeue()
#     elif(choice==3):
#                 if not queue:
#                     print("Queue is empty")
                
#                 else:
#                     print(len(queue))
#     else:
#         break;

#Program for implementation of queues using collections dequeue

# from collections import deque

# queue = deque()

# queue.append(10)
# queue.append(20)
# queue.append(30)
# queue.append(40)
# queue.append(50)

# print("Initial queue")
# print(queue)
# queue.popleft()
# queue.popleft()
# queue.popleft()
# queue.popleft()
# queue.popleft()
# print("Final queue")
# print(queue)
# #queue.popleft() if this is run again it will return an error saying queue is empty



#Queue implementation using queue library

from queue import Queue

queue = Queue()

queue.put(3)
queue.put(9)
queue.put(8)

print(queue.get())
print(queue.get())
print(queue.get())

print("Empty : \n",queue.empty())
print("Full : \n",queue.full())

























