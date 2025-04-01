"""You want to be safe online and use different passwords for different websites.
 However, you are forgetful at times and want to make a program that can match which password
 belongs to which website without storing the actual password!

This can be done via something called hashing. Hashing is when we take something and convert it into a different, 
unique identifier. This is done using a hash function. Luckily, there are several resources that can 
help us with this.

For example, using a hash function called SHA256(...) something as simple as

hello

can be hashed into a much more complex

2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824

Fill out the login(...) function for a website that hashes their passwords. Login should return True if an email's
 stored password hash in stored_logins is the same as the hash of password_to_check.

(Hint. You will need to use the provided hash_password(...) function. You don't necessarily
 need to know how it works, just know that hash_password(...) returns the hash for the password!)"""


import hashlib

def hash_password(password):
    """Hashes the password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

def login(email, password_to_check, stored_logins):
    """
    Checks if the provided email and password_to_check match the stored credentials.
    
    Args:
        email: The email to check in stored_logins.
        password_to_check: The password to verify.
        stored_logins: A dictionary where keys are emails and values are hashed passwords.
    
    Returns:
        bool: True if the hashed password_to_check matches the stored hash, False otherwise.
    """
    if email in stored_logins:
        stored_hash = stored_logins[email]
        input_hash = hash_password(password_to_check)
        return stored_hash == input_hash
    return False

# Example usage:
stored_logins = {
    "user@example.com": "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824",  # hash of "hello"
    "another@example.com": "d74ff0ee8da3b9806b18c877dbf29bbde50b5bd8e4dad7a3a725000feb82e8f1"   # hash of "world"
}

# Test cases
print(login("user@example.com", "hello", stored_logins))  # True
print(login("user@example.com", "wrong", stored_logins))  # False
print(login("nonexistent@example.com", "hello", stored_logins))  # False