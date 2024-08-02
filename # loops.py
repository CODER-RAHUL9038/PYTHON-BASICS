# # loops
# #while loop
# count=100000000000000000000000000
# while count>1:
   
#    count -=1
#    print("RAHUL MAHARAJ KI JAI","RAHUL MAHARAJ KI JAI","RAHUL MAHARAJ KI JAI","RAHUL MAHARAJ KI JAI","RAHUL MAHARAJ KI JAI",count)
# print(count)
#PRINT NO FROM 1 TO 100

# i=1
# while i<100:
#     i+=1
#     print(i)

# PRINT NO FROM 100 TO 1

# i=100
# while i>=1:
#     print(i)
#     i-=1
# print("Not possible")

#Print the multiplication table of any n number

# i=1
# n=int(input("enter the number :"))
# while i<=20:
#     print(n*i)
#     i+=1

# i=1
# # while i<=10:
# #     print(i*i)
# #     i+=1

tup=(1,4,9,16,25,36,49,64,81,100)
x=6
i=0
while i<len(tup):
    if tup[i]==x:
        print("The no is found at index", i)
        break
    i+=1
    
else:
    print("not found")