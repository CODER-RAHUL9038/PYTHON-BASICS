# # # last= [20,44,"rahul", 70.0]
# # # last[0]= 90
# # # print(list [0:])
# # list= [2,1,3,3]
# # # list.append(3)
# # # list.reverse()
# # # list.insert(0,50)
# # list.remove(3)
# # print(list)


# # tup=(9,5,5,3)
# # print(type(tup))

# #wap to take favourite movie name from user and create a list out of them
# # movie=[]
# # movie.append(input("enter the moie name:"))
# # movie.append(input("enter the 2nd name:"))
# # movie.append(input("enter the third name:"))
# # print(movie)

# #wap to check for palindrome in a list
# list1= [1,2,3,2,1]
# list2=list1.copy()
# list2.reverse()
# print(list2)
# print("the list is palindrome") if list1==list2 else print("the list is not palidrome, sorry")
# print(list2)

 #WAP TP COUNT THE NO OF STUDENT WITH THE A GRADE IN THE FOLLOWING TUPPLE ("C", "D", "A", "A", "B", "B", "A")
tup=["C", "D", "A", "A", "B", "B", "A"]
tup.sort()
print("The sorted list is",tup)
print("THE NO OF STUDENT WITH THE A GRADE are:" , tup.count("A") )
