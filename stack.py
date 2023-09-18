stack = [] 
def push():
    element =input("enter the element: ")
    stack.append(element)
    print(stack)
def pop_element():
    if not stack:
        print("stack is empty! ")
    else:
        e = stack.pop()
        print("removed element!",e)
        print(stack)

while True:
    print("select the opreation 1.push 2.pop 3.quit")
    choise = int(input())
    if choise == 1:
        push()
    elif choise==2:
        pop_element()
    elif choise==3:
        break
    else:
        print("enter the correct opretion ")

