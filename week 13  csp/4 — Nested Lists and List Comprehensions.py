# fruits =     ["apple", "orange", "banana", "coconut"]
# vegetables = ["celery", "carrot", "potatoes"]
# meats =      ["chicken", "fish", "turkey"]

# groceries = [fruits, vegetables, meats]

# print(groceries[1])

# print(groceries[0][0])
# print(groceries[1][2])
# print(groceries[2][2])

# groceries = [["apple", "orange", "banana", "coconut"],["celery", "carrot", "potatoes"],["chicken", "fish", "turkey"]]

# for collection in groceries:
#     for food in collection:
#         print(food)


# num_pad = ((1,2,3),(4,5,6),(7,8,9),("*",0,"#"))

# for row in num_pad:
#     for num in row:
#         print(num, end=" ")
#     print()




# Objective:
# Students will manipulate nested lists and understand basic list comprehensions.

# Key Notes:

# A list can contain other lists.

# List comprehensions provide a concise way to create lists.

# Examples:Objective:
# Students will manipulate nested lists and understand basic list comprehensions.

# Key Notes:

# A list can contain other lists.

# List comprehensions provide a concise way to create lists.

# Examples:

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# print(matrix[1][2])    # 6

# # List comprehension
# first_col = [row[0] for row in matrix]
# print(first_col)       # [1, 4, 7]



# Practice Problems:

# Build a matrix variable containing 3 lists of 3 numbers each.

# Print the first list.

# Print the second item from the third list.

# Use a list comprehension to extract the last item from each sub-list.

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0])
print(matrix[2][1])

last_item = [row[2]for row in matrix]
print(last_item)





# Challenge: Create a new list containing squares of numbers from 1–10 using a comprehension.


squares = [x**2 for x in range(1, 11)]
print(squares)