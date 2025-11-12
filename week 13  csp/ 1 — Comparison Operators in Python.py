# Objective:
# Students will learn how to compare values using Python’s comparison operators and interpret Boolean results.

# Topics Covered:
# ==, !=, >, <, >=, <=

# Key Notes:

# Comparison operators compare two values and return either True or False.

# Remember: = is assignment, while == is comparison.

a = 3
b = 4

print(a == b)   # False
print(a != b)   # True
print(a > b)    # False
print(a < b)    # True
print(a >= b)   # False
print(a <= b)   # True


#predict the output of the following comparisons:
10 > 5    #true
7 == 2 * 3 + 1    # true
8 != 8   #false
4 <= 2 + 2   #true

# Write 3 examples that result in True and 3 that result in False.
4 > 2
24 == 10 * 2 + 4
38 != 17

5 <= 2
10 == 5 * 3
14 > 29



# Create a simple grade-checking condition:

# practice problem :
# where a student must check if their score is greater than or equal to 60 to pass a test.# The password must be at least 8 characters long and contain at least one digit.password = "mypassword1"


name = input("What is your name? ")

password = str(input("What is your password? "))

# if len(password) < 8:
#         print("Password must be at least 8 characters long and contain at least one digit.")
        
# else :
#    print()

grade = int(input("What did you score on the test? "))

if grade >= 90 and grade <= 100:
        print("Good job", (name), "you got an A")
elif grade >= 80 and grade <= 89 :
    print((name), "You got a B")
elif grade >= 70 and grade <= 79 :
    print((name), "You got a C")
elif grade >= 60 and grade <= 69 :
        print ("Sorry", (name), "you got a D")
else :
      print((name), "you failed")


