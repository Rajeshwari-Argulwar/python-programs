# write a python program which will keep adding a stream of numbers inputted by the user. the adding stops as soon ass user presses q key on the keyboard
sum = 0
while(True):
    userInput = input("Enter the price: \n")
    if(userInput!='q'):
        sum = sum + int(userInput)
        print(f"total bill so far: {sum}")

    else:
        print(f"your total bill is {sum}")
        print("Thanks for shopping")
        break
