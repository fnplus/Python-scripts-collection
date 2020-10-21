n = 0
last_char = ""
last_last_char = ""

with open("file.txt", "r") as f:
    for line in f:
        n += 1
        if last_char == "\n":
            if last_last_char == "\n":
                print(n - 1)
        last_last_char = last_char
        last_char = line
