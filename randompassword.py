import secrets
import string
def generate_password(length: int) -> str:
    # Define the characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Use secrets.choice to generate a secure random password
    password = ''.join(secrets.choice(characters) for i in range(length))
    return password
# Example usage
password_length = 12
password = generate_password(password_length)
print(f'Generated password: {password}')