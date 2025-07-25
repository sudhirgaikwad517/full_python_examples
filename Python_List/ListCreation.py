list1 = [] #creating empty list

list2 = [1,2,3,4,5,6] #creating list with 6 elements

list3 = [1,2,3,4,"Sonu",True , 4.5 , 4.00] #list can conatin multiple datatypes

print(list1)
print(list2) #printing the list
print(list3) #printing the list
print(type(list1)) #printing the type

print(list3[4],list3[5]) # accessing list element by the index number

print(list3[len(list3)-4]) #accessing the element by negative index

print(list3[:2]) # accessing the list element by slicing


print(list3[: :2])

#list comprehension 

even_list = [item for item in list3 if isinstance(item,(int , float)) and item % 2 == 0]

print(even_list)

word_with_S = [item for item in list3 if isinstance(item,(str)) and "S" in item]

print(word_with_S)

