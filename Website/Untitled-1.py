import random
import string 

passlen = int(input("Enter password length: "))
complexity = int(input("Enter password complexity 1-4: "))
def generate_pass(length, complex):
    allowedlets = ""
    if complex == 1:
        allowedlets += string.ascii_lowercase
    elif complex == 2:
        allowedlets += string.ascii_lowercase
        allowedlets += string.ascii_uppercase
    elif complex == 3:
        allowedlets += string.ascii_lowercase
        allowedlets += string.ascii_uppercase
        allowedlets += string.digits
    else:
        allowedlets += string.ascii_lowercase
        allowedlets += string.ascii_uppercase
        allowedlets += string.digits
        allowedlets += string.punctuation
    password = "".join(random.choice(allowedlets) for i in range(length))
    return password

print(generate_pass(passlen, complexity))