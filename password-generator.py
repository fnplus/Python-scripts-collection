import random
import string
passlen = random.randint(10,20)
password=''
string.ascii_letters
'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*'
password=''.join(random.choices(string.ascii_letters,k=passlen))
print("Your password is:-",str(password))
