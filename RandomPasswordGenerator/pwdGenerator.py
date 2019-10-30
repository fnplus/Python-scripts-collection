import random

LOWERCASE_CHARS = tuple(map(chr, range(ord('a'), ord('z')+1)))
UPPERCASE_CHARS = tuple(map(chr, range(ord('A'), ord('Z')+1)))
DIGITS = tuple(map(str, range(0, 10)))
SPECIALS = ('!', '@', '#', '$', '%', '^', '&', '*')

SEQUENCE = (LOWERCASE_CHARS,
            UPPERCASE_CHARS,
            DIGITS,
            SPECIALS,
            )

def generate_random_password(total, sequences):
    r = _generate_random_number_for_each_sequence(total, len(sequences))

    password = []
    for (population, k) in zip(sequences, r):
        n = 0
        while n < k:
            position = random.randint(0, len(population)-1)
            password += population[position]
            n += 1
    random.shuffle(password)
    
    while _is_repeating(password):
        random.shuffle(password)
        
    return ''.join(password)

def _generate_random_number_for_each_sequence(total, sequence_number):
    current_total = 0
    r = []
    for n in range(sequence_number-1, 0, -1):
        current = random.randint(1, total - current_total - n)
        current_total += current
        r.append(current)
    r.append(total - sum(r))
    random.shuffle(r)

    return r

def _is_repeating(password):
    n = 1
    while n < len(password):
        if password[n] == password[n-1]:
            return True
        n += 1
    return False

if __name__ == '__main__':
    length = int(input("Enter the length of password to be generated : "))

    if length < 8 or length > 30:
        print("\nLength fo password should be between 8 and 30. Generating password of random length...\n\n")
        print(generate_random_password(random.randint(6,30), SEQUENCE))
    else :
        print(generate_random_password(length, SEQUENCE))