import string
import random
import argparse
import sys
import pyperclip

parser = argparse.ArgumentParser(description="Password Generator")
parser.add_argument('-s', '--service', type = str, help = "Name of the Website where u want to use it", default='Facebook')
parser.add_argument('-l', '--len', type = int, help = "Length of the Password", default=8)
parser.add_argument('-sm', '--small', type = int, help = "Number of lower case characters", default=2)
parser.add_argument('-bg', '--big', type = int, help = "Number of upper case characters", default=2)
parser.add_argument('-nm', '--number', type = int, help = "Number of digits", default=2)
parser.add_argument('-sc', '--special', type = int, help = "Number of special characters", default=2)
args = parser.parse_args()

def passgen(service, len, small, big, number, special):
    k1 = string.ascii_lowercase
    k2 = string.ascii_uppercase
    k3 = string.digits
    k4 = string.punctuation

    m1 = list(k1)
    m2 = list(k2)
    m3 = list(k3)
    m4 = list(k4)

    random.shuffle(m1)
    random.shuffle(m2)
    random.shuffle(m3)
    random.shuffle(m4)

    m5 = m1[:small]
    m6 = m2[:big]
    m7 = m3[:number]
    m8 = m4[:special]

    p = []

    p.extend(m5)
    p.extend(m6)
    p.extend(m7)
    p.extend(m8)
    p.extend(m1)
    p.extend(m2)
    p.extend(m3)
    p.extend(m4)

    pd = p[:len]

    password = "".join(pd)

    print(password)
    pyperclip.copy(password)

    file = open("passwords.txt", 'a')
    file.write(service)
    file.write(" : ")
    file.write(password)
    file.write('\n')
    file.close
    

if __name__ == '__main__':
    passgen(args.service, args.len, args.small, args.big, args.number, args.special)
