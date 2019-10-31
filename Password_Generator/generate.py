from random import choice
from string import printable


def random_password(length):
    """
    Provides a random password of the given length.

    :param int length: The length of the password to generate.
    """

    return "".join([choice(printable) for x in range(int(length))])


if __name__ == "__main__":
    amount = int(input("How many passwords: "))
    number = int(input("Length of password? "))

    for i in range(1, amount + 1):
        print(f"   Password: {i} - {repr(random_password(number))} ")
