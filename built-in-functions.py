phase = "Hello"
print(phase)
print(phase.lower())
print(phase.upper())
print(phase.isupper())
print(phase.islower())
print(len(phase))
print(phase.index("o"))
print(phase.replace("Hello","hi"))

friends=["hi","hi","hfhf","jnfndef","dkdgjd"]
lucky_numbers = [4,5,78,85,45,75,5454,574,549]
#friends[1]="vgj"
print(friends)
print(friends[1])
print(friends[1:]) #[1] will be skipped others will be printed

print(friends.append("creed")  )   # adding to the list
print(friends)
print(friends.insert(1,"gjgjgj")) #gjgjgj will be on 1st position
print(friends)
print(friends.remove("hfhf") )    #remove
print(friends)
print(friends.pop())   #last element will be poped out if we print list last one will not be their
print(friends)
print(friends.index("hi"))   #index of hi
print(friends.count("hi"))    #count number of times hi present 

print(lucky_numbers.sort()) #assending order
print(lucky_numbers)
print(lucky_numbers.reverse())
print(lucky_numbers)
friends2=friends.copy()
print(friends2)
print(friends.extend(lucky_numbers))  # joined two diffrent list together
print(friends)

print(friends.clear())  #reset /empty every thing