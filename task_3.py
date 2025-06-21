# Password Generator Program in Python
# Created by Abhinav during CodSoft Internship

import random
import string

def generate_password():
    print("Welcome to the Password Generator!")
    try:
        length = int(input("Enter the desired password length: "))

        if length < 4:
            return "Password length should be at least 4."

        # Using letters, digits and punctuation to create strong password
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        
        return f"Generated Password: {password}"

    except ValueError:
        return "Invalid input! Please enter a valid number."

# Run the generator
print(generate_password())