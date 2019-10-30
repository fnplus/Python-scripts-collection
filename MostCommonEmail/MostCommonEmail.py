# Seeking email that sent the most emails from email logs (text file)

# 1. Request file name
fname = raw_input('Enter file name: ')

# 2. File handle
fhandle = open(fname)

# 3. Create dictionary
counts = dict()

# 4. Variable: first word to look for in each sentence
x = 'From'

# 5. Loop through each sentence
for line in fhandle:
    # 6. Create list
    words = line.split()

    # 7. Guardian pattern for empty lines
    if len(words) < 1:
        continue

    # To ignore all sentences starting from "From:"
    # if words[0] == 'From:':
    #     continue

    # 8. Ignore all other than x
    if words[0] != x:
        continue

    # print words
    # shows position 2 has the emails

    email = words[1]

    # 9. Map key-value pairs to dictionary
    counts[email] = counts.get(email, 0) + 1

    # print counts
    # shows you have a dictionary with key-value pairs of format email:count

# 10. Convert dictionary to list of tuples
counts = counts.items()

# 11. Loop through lists to convert to value-key tuples
lst = list()
for k, v in counts:
    lst.append((v, k))

lst = sorted(lst)

# Least common
print lst[0]

# Most common
print lst[-1]
