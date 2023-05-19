from string import ascii_lowercase, ascii_uppercase, digits

from random import randint


def generate_random_password(length):
    password = ""
    strange_group = "/|-_)(*&^%$#@!~*)"
    groups = [ascii_lowercase, ascii_uppercase, digits, strange_group]
    for i in range(length):
        group = groups[randint(0, len(groups)-1)]
        letter = group[randint(0, len(group)-1)]
        password += letter
    return password
print(generate_random_password(8))