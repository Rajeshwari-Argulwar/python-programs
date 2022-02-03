def sayhi():
    print("hello")

def chat():
    print("This is a calculator")

def exit():
    print("Thank you")

def mul(n1,n2):
    return n1*n2

def add(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2

def div(n1,n2):
    return n1/n2    
sayhi()
chat()
i = int(input("Enter a number:- "))
j = int(input("Enter another number:- "))
print("Addition :-")
print(add(i,j))
print("Substraction :-")
print(sub(i,j))
print("Multiplication :-")
print(mul(i,j))
print("Division :-")
print(div(i,j))
exit()

