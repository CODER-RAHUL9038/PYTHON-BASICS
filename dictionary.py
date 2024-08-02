# # # dic= {
# # #     "name": "Rahul",
# # #     "cgpa": 8.62,
# # #     "age": 25,
# # # }
# # # dic["name"]="KING"
# # # print(dic["name"])

# # # #nested dictionary

# # course= {
# #     "subject":
# #     {
# #         "phy":97,
# #         "che":98,
# #         "bio":100,
# #     },
# #     "age":25,
# # }

# # # print(course["subject"]["che"])
# # course.update({"Rahul":"God", "class": 10,"age":97000})
# # print(course)

#     #set
# # num={1,1,2,2,3,4} 
# # num.add(6)     
# # print(num.pop())
# # print(num.pop())
# # print(num)   

# # set1={1,2,3}
# # set2={3,4,5}
# # print(set1.intersection(set2))

# # dic= {
# #     "table":["a piece of furniture", "list of facts and figure"],
# #     "cat": "a small animal",

# # }
# # print(dic)


# # sub1={"python", "java", "c++","python","javascript"}
# # sub2={"python", "java", "c++","java","c"}
# # classroom=sub1.union(sub2)
# # print(classroom)
# # print("The no of classroom needed is ",len(classroom))
# #wap to take three subjects marks from user and store the in dictionary
# #One way
# # dic={}
# # che=input("enter the marks of chemistry:")
# # dic={"chemistry":che}
# # phy=input("enter the marks of physics:")
# # dic={"chemistry":che,"physics":phy}
# # math=input("enter the marks of Mathematics:")
# # dic={"chemistry":che,"physics":phy,"maths":math}

# #using update method
# mark={}
# x=int(input("enter the marks of chemistry:"))
# mark.update({"chemistry":x})

# y=int(input("enter the marks of physics:"))
# mark.update({"physics":y})

# z=int(input("enter the marks of biology:"))
# mark.update({"biology":z})
# print(mark)
set={(9,9.0)}
print(type(set))