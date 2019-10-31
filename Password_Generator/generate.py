import random
import string


def randompassword(number):
	chars = random.sample(string.ascii_lowercase + string.digits, number)
	passw = ''.join(map(str, chars))
	return passw


amount = int(input("How many passwords:\n"))
number = int(input("Lenght of password?\n"))
for i in range(amount):
	print(f"   Password: {i} - {randompassword(number)} ")
