import random
import string

# Get password length from user
length = int(input("Enter the desired password length: "))

# Define characters to use
characters = string.ascii_letters + string.digits + string.punctuation

# Generate password
password = ""
for i in range(length):
    password += random.choice(characters)

# Display the generated password
print("Generated Password:", password)
