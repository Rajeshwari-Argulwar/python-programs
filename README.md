# python-programs
 some practice programs made by useing python programming language



some notes


syntax

charecter variable :- charecter_name ="john"
integer variable:- integer_name = 50 (we can directly put integer or floting point number without declaring it with its data type)
boolien :- isok = True
while useing :- + charecter/integer_name(we can update it later same as it is)

                            STRING

functions to work on stings
phrase="Hello"
e.g. print("hello World")

1)print(phase+"is cool")        //concatination
2)print(phase.lower())          // converting to lower case
3)print(phase.upper())          // converting to upper case
4)print(phase.isupper())        // checking if string is in upper case
5)print(len(phase))             // counting length of string
6)print(phase[0])               //give alphabet on 0th position
7)print(phase.index("H"))       // give index position of that H/llo/ello etc.
8)print(phase.replace("Hello,"Hi"))//replace hello with hi


                              NUMBERS
directly like this
1)print(2) 
2)print(2.36547854)
3)print(-2.45865)
4)print(3+4)
5)print(5-8)
6)print(7*2)
7)print(4/6)
8)print(3+4.8)
9)print(3*4+5)
10)print(3*(4+5))
11)print(10%5)
12)my_num = -5 
   print(my_num)
13)print(str(my_num)) // number is converted into a string
14)print(str(my_num)+ "my favorite number")
15)print(abs(my_num))  // will give absolute value of my_num
16)print(pow(3, 2)) // ~  3^2
17)print (max(4,8))  // largest of all
18)print (min(4,8))   //smallest of all
19)print (round(4.1)) //round the number like it is 4
20)        from math import *
	print (floor(4.6)) // cuts the decimal point
	print (ceil(4.2)) // no matter what is infront it will print rounded value
	print (sqrt(36)) // squre-root


                           INPUT
name = input("Enter your name:")
age  = input("Enter your age:")
print("hello "+ name+ "! You are"+ age)



				CALCULATOR

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = int(num1) + int(num2)//python by default take input as string so we added int to clarify things
print(result)

// we can use float insted of int


                            mad libs game



				LIST

friends=["hi","hi","hfhf","jnfndef","dkdgjd"]
lucky_numbers = [4,5,78,85,45,75,5454,574,549]
friends[1]="vgj"
1)print(friends)
2)print(friends[1])
3)print(friends[1:]) //[1] will be skipped others will be printed
4)friends.extend(lucky_numbers)  // joined two diffrent list together
5)friends.append("creed")     // adding to the list
6)friends.insert(1,"gjgjgj") //gjgjgj will be on 1st position
7)friends.remove("hfhf")     //remove
8)friends.clear()  //reset /empty every thing
9)friends.pop()   //last element will be poped out if we print list last one will not be their
10)friends.index("hi"))   //index of hi
11)friends.count("hi)) //count number of times hi present 
12)friends.sort() //assending order
13)lucky_numbers.sort()
14)lucky_numbers.reverse()
15)friends2 = friends.copy()  //copy list



				TUPPLES
coordinate =( 4,5)  // we cant change it later
print(coordinate[0])
we can change if touple is in list like co=[(4,6),(4,9),(7,5)]




				FUNCTION
code inside function need to be indented //like same space in each row
def sayhi():
    print("hello user")
print("Top")
sayhi()
print("bottom")



def say_hi(name,age):
    print("hello"+ name+"your " + age)
say_hi("mike","52")
say_hi("mi","35")

		


				RETURN

def cube(num)
	return num*num*num
result =cube(4)
print(result)


				IF STATEMENT
if condition or condition:
			statement
if condition and condition:
			statement

      	












