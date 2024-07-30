import random
import string

def generate_password(length):
    if length < 4:
        print("Password length should be at least 4 characters.")
        return None
    
    letters = string.ascii_letters  # a-z, A-Z
    digits = string.digits          # 0-9
    special_chars = string.punctuation  # Special characters
    
    all_chars = letters + digits + special_chars
    
    password = [
        random.choice(letters),
        random.choice(digits),
        random.choice(special_chars)
    ]
    
    password += random.choices(all_chars, k=length-3)
    
    random.shuffle(password)    # Shuffle the password 

    return ''.join(password)

def main():
    try:
        length = int(input("Enter password length: "))
    except ValueError:
        print("Invalid input!")
        return
    
    password = generate_password(length)
    
    if password:
        print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()