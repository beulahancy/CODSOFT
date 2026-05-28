import random
import string

def generate_password(length):
    
    letters = string.ascii_letters   
    digits = string.digits           
    symbols = string.punctuation     

    
    all_characters = letters + digits + symbols

    
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password


try:
    length = int(input("Enter the desired password length: "))
    
    if length <= 0:
        print("Please enter a positive number.")
    else:
        password = generate_password(length)
        print("Generated Password:", password)

except ValueError:
    print("Invalid input! Please enter a number.")