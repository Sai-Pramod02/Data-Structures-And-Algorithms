#Implementing of priority queue using list

# queue = []
# queue.append(5)
# queue.append(4)
# queue.append(10)
# queue.append(6)

# queue.sort()  #Sorts the queue in ascending order///  queue.sort(reverse=True) sorts the queue in descending order

# print(queue.pop(0))
# print(queue.pop(0))
# print(queue.pop(0))
# print(queue.pop(0))


#Implementing priority using PriorityQueue module

# import queue

# queue = queue.PriorityQueue()
 
# queue.put(5)
# queue.put(0)
# queue.put(3)
# queue.put(9)
# queue.put(7)

# print(queue.get())
# print(queue.get())
# print(queue.get())
# print(queue.get())
# print(queue.get())

#Implementing Priority queue using Tuple

queue = []
queue.append((1,"Riya"))
queue.append((3,"Pramodh"))
queue.append((2,"Pramod"))
queue.sort()

print(queue)