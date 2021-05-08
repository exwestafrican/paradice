from random import choice
from string import ascii_letters, digits


class Utils:
    def generate_prd_code(length=6):
        token = "".join([choice(ascii_letters + digits) for i in range(length - 1)])
        return "PRD-{}".format(token)
