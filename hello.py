print("Hello World!")
name = input("What's your name? ")

#remove whitespaces from str and capitalize first letter

#Remove whitespaces from str and capitalize first letter of every word\
name = name.strip().title()

#implement these functions right into the input
name = input("What's your name? ").lower()

#split user's name into first name and last name
first, last = name.split(" ")
print(f"Hello, {name}")
print(first, last)
# Comment

"""
This is a long comment

"""
