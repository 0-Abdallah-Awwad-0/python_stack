# 1. Print "Hello World"
print("Hello World")

# 2. Print "Hello Noelle!" using a variable
name = "Noelle"

# with a comma
print("Hello", name + "!")

# with +
print("Hello " + name + "!")


# 3. Print "Hello 42!" using a number variable
fav_number = 42

# with a comma
print("Hello", str(fav_number) + "!")

# with + 
# This gives an error because fav_number is a number, not a string
# print("Hello " + fav_number + "!")

# Bonus fix: convert the number to a string
print("Hello " + str(fav_number) + "!")


# 4. Print "I love to eat sushi and pizza."
fave_food1 = "sushi"
fave_food2 = "pizza"

# with .format()
print("I love to eat {} and {}.".format(fave_food1, fave_food2))

# with f-string
print(f"I love to eat {fave_food1} and {fave_food2}.")