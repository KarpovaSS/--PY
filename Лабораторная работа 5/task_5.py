from random import sample
import string

def get_random_password(n=8) -> str:
    str_ = string.ascii_letters + string.digits
    return ''.join(sample(str_, n))

print(get_random_password())
