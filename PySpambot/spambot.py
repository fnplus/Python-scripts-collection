import pyautogui, time

print("Welcome to spambot.py\n")
try:
    text = input("Enter your text you want to spam:\n")
    loop = int(input("Number of times to spam:\n"))

except KeyboardInterrupt:
    print("Exiting the program..\n")

if loop == "":
    print("Ok, initialising while loop, got 10 seconds to open your text field\n")
    time.sleep(10.00)
    try:
        while True:
            pyautogui.typewrite(text)
            pyautogui.press('enter')

    except KeyboardInterrupt:
        print("Exiting the program....")

elif loop != "":
    print("Ok, initialising for loop, got 10 seconds to open your text field\n")
    time.sleep(10)
    try:
        for i in range(int(loop)):
            pyautogui.typewrite(text)
            pyautogui.press('enter')

    except KeyboardInterrupt:
        print("Exiting the program....")