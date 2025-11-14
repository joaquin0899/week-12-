# Objective:
# Students will understand how to create, modify, and access elements in Python lists.

# Topics Covered:
# Creating lists, indexing, slicing, appending, popping, sorting, reversing.
# lists are part of the collection family in python
# Examples:

# my_list = [1,2,3,4,5]
# print(my_list)
# print(len(my_list))
# print(type(my_list))
# print(my_list[0])
# print(my_list[1:4])
# print(my_list[1:])
# print(my_list[:-1])
# print(my_list[::-1])
# my_list.append(6)
# print(my_list)
# my_list.extend([7,8])
# my_list.extend([9,10,11])
# print(my_list)
# my_list.pop()
# print(my_list)
# my_list.pop()
# print(my_list)
# my_list.reverse()
# print(my_list)
# my_list.reverse()
# print(my_list)
# my_list.remove(9)
# print(my_list)

# new_list = list(range(12,120))
# print(new_list)

# my_list.extend(new_list)
# print(my_list)

# long_list = list(range(120, 500))
# my_list.extend(long_list)
# print(my_list)

# every_third_element = my_list[::3]
# print(every_third_element)

# print(my_list[::10])

# del my_list[::3]
# print(my_list)


# .append - adds one to list
# .extend - adds multiple to list
# .pop - removes one from end of list
# .remove - removes first occurence of value
# .sort - sort in ascending order
# .reverse -reverse order of list

# why is a list more useful than a variable
# A list can hold multiple values
# variable can only hold one at a time

# cakes = [ 'chocolate', 'vanilla', 'red velvet', 'carrot']
# print(cakes)
# print(cakes[0])
# print(cakes[-1])

# cakes[0] = "strawberry"

# print(cakes)

# cakes.pop()
# print(cakes)

# cakes.append('lemon')
# print(cakes)

# cakes.insert(2, 'funfetti')
# print(cakes)

# cakes.extend(['oreo', 'chocolate'])
# print(cakes)

# cakes.sort()
# print(cakes)


# my_list = ['apple', 'banana', 'cherry']
# print(my_list[0])         # apple
# print(my_list[1:])        # ['banana', 'cherry']

# my_list.append('grape')
# print(my_list)

# my_list.pop(1)
# print(my_list)

# numbers = [3, 1, 4, 2]
# numbers.sort()
# print(numbers)


# # Practice Problems:

# # Create a list with 5 of your favorite foods.

fav_foods = ['pizza', 'tacos', 'chicken', 'fries', 'burgers']





# # Print the second and last item.
print(fav_foods[1])
print(fav_foods[-1])
# Add a new item using .append().

fav_foods.append("cake")
print(fav_foods)


# Remove the first item using .pop(0).
fav_foods.pop(0)
print(fav_foods)
# Reverse your list using .reverse().
fav_foods.reverse()
print(fav_foods)
# Create a list of 3 lists (matrix), and access the middle element.]

#set = {1,2,3}
#sets are unordered, do not support index or slicing, you can remove or add, use {}, no duplicates

my_set = {1,2,3,4,5}
print(my_set)
print(type(my_set))

my_set.add(6)
print(my_set)

my_set.remove(3)
print(my_set)

print(4 in my_set)
print(3 in my_set)



#tuples are ordered, cant modify them after creation, use ()

my_tuples = (1,2,3,4,5)
print(my_tuples)
print(type(my_tuples))
print(my_tuples[0])
print(my_tuples[1:4])

