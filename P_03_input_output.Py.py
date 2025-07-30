# ask the user for their name
username = input("what is your name? ")

# ask the user their favorite number (integer)
fav_num = int(input("what is your favorite number? "))

# Double, halve and square the users favorite number
double = fav_num * 2
halve = fav_num / 2
square = fav_num * fav_num

# Greet the user
print()
print(f"Hi {username}, your favorite number is {fav_num}")

# Output the results of doubling, halving and
# squaring their favorite integer
print(f"Double {fav_num} is {double}.")
print(f"half {fav_num} is {halve}")
print(f"{fav_num} squared is {square}")
print()
print("have a nice day")
