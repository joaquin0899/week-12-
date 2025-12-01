# Objective:
# Apply comparison and logical operators to a real-world problem.

# Scenario:
# Write a program that:

# Asks the user for today’s temperature.

# Prints whether it’s cold, warm, or hot using comparison operators.

# If the temperature is out of range (below -10 or above 110), display “Extreme temperature warning!”

# Starter Code:

temp = int(input("What is the weather today? "))

if temp >=110 or temp <=-10:
    print ("Extreme temperature warning!")
elif temp >=-9 and temp <=59:
    print("The weather is cold out")
elif temp >=60 and temp <= 89:
    print("The weather is warm out")
elif temp >=90 and temp <=109:
    print("The weather is hot out")

