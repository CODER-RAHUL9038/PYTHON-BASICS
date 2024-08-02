# # n1 = 10
# # n2 = 5
# # n3 = 200
# # n4 = 40000

# # if (n1 > n2 and n1 > n3 and n1>n4):
# #     print("The greatest number is:", n1)
# # elif n2 > n1 and n2 > n3 and n2>n4:
# #     print("The greatest number is:", n2)
# # elif n3 > n1 and n3 > n2 and n3>n4:
# #     print("The greatest number is:", n3)
# # else:
#     print("The greatest number is:", n4)


 #using nested if
# Define the numbers
# Take user input for four numbers
n1 = float(input("Enter the first number: "))
n2 = float(input("Enter the second number: "))
n3 = float(input("Enter the third number: "))
n4 = float(input("Enter the fourth number: "))



# Assume the first number is the greatest
greatest = n1

# Compare with the second number
if n2 > greatest:
    greatest = n2

# Compare with the third number
if n3 > greatest:
    greatest = n3

# Compare with the fourth number
if n4 > greatest:
    greatest = n4

# Print the greatest number
print("The greatest number is:", greatest)
