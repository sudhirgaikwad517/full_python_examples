list1 = [] #creating empty list

list2 = [1,2,3,4,5,6] #creating list with 6 elements

list3 = [1,2,3,4,"Sonu",False , 4.5 , 4.00] #list can conatin multiple datatypes

# for i in list3:
#     print(i , end=" ") # iterating list using for loop 

# for i in range(len(list3)):
#                   item = list3[i]
#                   print(item , end=" ") #iterating list by the len method 

#iterating list by enumerate method 

# for index , item in enumerate(list3):
#     print(f"Index : {index} , Item : {item}")

# iterating the element using while loop

# try:
#     i=0
#     while i <= len(list3):
#         print(list3[i])
#         i += 1
#         if i == len(list3):
#             print("List iteration is complete.")
# except Exception as e:
#     print("Some issue is there wait for some time ." , " Error is :" , e)

#removing the element form the list using while loop
    
# try:
#     while list3:
#         list3.remove(list3[0])
#     if not list3:
#             print("All elementd removed successfuly .")
#     print(list3)
# except Exception as e:
#     print("Some issue is there wait for some time ." , " Error is :" , e)

