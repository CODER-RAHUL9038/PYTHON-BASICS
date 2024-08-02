# #NESTING
# age=90
# if age>=18:
#     if age<80:
#         print("can drive")
#     else:
#         print("cannot drive")
# else:
#     print("cannot drive")
#wap to find the greatest of 3 numbers enter by the user
n1= input("ENTER THE FIRST NUMBER: ")
n2= input("ENTER THE SECOND NUMBER: ")
n3= input("ENTER THE THIRD NUMBER: ")
if (n1>n2 and n1>n3):
    print("The greatest number is :", n1 )
elif n2>n3:
    print("The greatest number is :", n2)
else:
    print("The greatest number is :", n3)