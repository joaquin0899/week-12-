# Objective:
# Students will understand how to create, modify, and access elements in Python lists.

# Topics Covered:
# Creating lists, indexing, slicing, appending, popping, sorting, reversing.
# lists are part of the collection family in python
# Examples:

my_list = [1,2,3,4,5]
print(my_list)
print(len(my_list))
print(type(my_list))
print(my_list[0])
print(my_list[1:4])
print(my_list[1:])
print(my_list[:-1])
print(my_list[::-1])
my_list.append(6)
print(my_list)
my_list.extend([7,8])
my_list.extend([9,10,11])
print(my_list)
my_list.pop()
print(my_list)
my_list.pop()
print(my_list)
my_list.reverse()
print(my_list)
my_list.reverse()
print(my_list)
my_list.remove(9)
print(my_list)

new_list = list(range(12,120))
print(new_list)

my_list.extend(new_list)
print(my_list)

long_list = list(range(120, 500))
my_list.extend(long_list)
print(my_list)

every_third_element = my_list[::3]
print(every_third_element)

print(my_list[::10])

del my_list[::3]
print(my_list)


# .append - adds one to list
# .extend - adds multiple to list
# .pop - removes one from end of list
# .remove - removes first occurence of value
# .sort - sort in ascending order
# .reverse -reverse order of list


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

# fav_foods = ['pizza', 'tacos', 'chicken', 'fries', 'burgers']





# # Print the second and last item.
# print(fav_foods[1])
# Add a new item using .append().

# Remove the first item using .pop(0).

# Reverse your list using .reverse().

# Create a list of 3 lists (matrix), and access the middle element.