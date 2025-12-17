import random
import string

def generate_random_password(length=12):
    """
    Generates a random password of a specified length using lowercase letters, 
    uppercase letters, and digits.
    
    The password is then shuffled to ensure randomness.

    Args:
        length (int): The desired length of the password. Defaults to 12.

    Returns:
        str: A randomly generated password.
    """
    
    # Define the possible characters for the password
    characters = string.ascii_lowercase + string.ascii_uppercase + string.digits
    
    # Ensure the password has at least one of each character type for strength
    # Start with one of each type
    password_list = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits)
    ]
    
    # Fill the rest of the password length with a random selection from all characters
    if length > 3:
        for _ in range(length - 3):
            password_list.append(random.choice(characters))
    elif length < 3:
        # If the requested length is less than 3, just use the first 'length' items
        password_list = password_list[:length]

    # Shuffle the list of characters to ensure true randomness and avoid patterns
    random.shuffle(password_list)
    
    # Join the list of characters into a single string
    password = "".join(password_list)
    
    return password

# Example usage:
new_password = generate_random_password(length=16)
print(f"Generated Password: {new_password}")
