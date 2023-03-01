stack = []
def push(element):
    if limit == len(stack):
        print("List is full")
    stack.append(element)
    print(stack)
def pop():
    if not stack:
        print('Stack is empty')
    else:
       element= stack.pop()
       print("removed : "+element)
limit = int(input("Enter the size of the stack"))
while True:
    print("Enter:1. for push \n 2. for pop \n 3. for quit")
    choice = int(input())
    if choice == 1:
        print("Enter the element to be pushed")
        element = int(input())
        push(element)
    elif choice == 2:
        pop()
    else:
        break;