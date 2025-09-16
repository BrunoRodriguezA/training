import re

cvv = '321'
regex = "^[0-9]{3}$"

p = re.compile(regex)


# if not re.fullmatch(r"\d{3}", cvv):
    # print('hola')

email = 'pepe@gmail.com'


# TLD top level domain

if not re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", email):
    print('email no valido')

# libreia email validator

