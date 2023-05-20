# main branch

from string import digits, ascii_lowercase, ascii_uppercase
from random import randint


def pass_gen(length: int):
    password = ""
    strange_group = "_-@&%$#!\/."
    groups = [digits, ascii_lowercase, ascii_uppercase, strange_group]
    for i in range(length):
        group = groups[randint(0, len(groups)-1)]
        password += group[randint(0, len(group)-1)]
    return password