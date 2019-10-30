#This is a passphrase generator based on the Diceware method of passphrase generation.

#Import random module and the Diceware Word list dictionary
import random
from DiceDictionary import DiceDict as DD
from DiceDictionary import SymbolList as SL
print("This is a passphrase generator based on the Diceware method of passphrase generation, "
      "\nyou will be asked how long you want your passphrase, and after generation, "
      "\nyou will be asked if you want to add a symbol, and after that if you want to add a number.")

#Ask user how long they want the passphrase to be
LengthValid = False
while LengthValid == False:

    Length = input("\nPlease enter how many words long you would like your passphrase \n(between 5-10, Recommended:7):")
    try:
        if int(Length) >= 5 and int(Length) <= 10:
            LengthValid = True
        else:
            print("That is not a valid number.")
    except ValueError:
        print("That is not a number.")
        continue


#Roll 5 dice, add their values to a list (Passwords)
Passwords = []
P = 1
while P <= int(Length): #Stop when there are X words (Defined by user) from the dictionary in the passphrase
    TotalRoll = []
    i = 1
    TR = 0
    TotalRollConcat = ""
    while i <= 5:
        Diceroll = random.randint(1,6)
        TotalRoll.append(Diceroll)
        i += 1
    #Concatenate the Dice rolls
    while TR != 5:
        TotalRollConcat += str(TotalRoll[TR])
        TR += 1
    #Grab the value with your generated key from the dictionary
    Word = DD[int(TotalRollConcat)]
    Passwords.append(Word)
    P += 1
#Concatenate the words in the password list
Passphrase = ""
pp = 0
while pp < int(Length):
    Passphrase += str(Passwords[pp])
    pp += 1
print("\n",Passphrase.capitalize())

#Check if user wants to add a random symbol/number/caps etc. into the passphrase, or if they want to save it to a text file.
inputValid = False
while inputValid == False:
        Symbol = input("\nHere is your passphrase. If you want to make it extra secure, \n"
                       "you can replace a random character with a random symbol \n"
                       "(You may wish to skip this if your generated password already has a symbol). (Y/N): ").lower()

        if Symbol == "y":
           Range = len(Passphrase) - 1
           Char = random.randint(0, Range)
           Sym = random.choice(SL)
           Passphrase2 = ""
           i = 0
           while i <= Range:
               if i != Char:
                   Passphrase2 += Passphrase[i]
                   i += 1
               elif i == Char:
                   Passphrase2 += Sym
                   i += 1
           Passphrase = Passphrase2
        elif Symbol == "n":
            inputValid = True
        else:
            print("That is not a valid answer")
            continue
        inputValid = True

print("\n",Passphrase.capitalize())
inputValid = False
while inputValid == False:

        number = input("\nWould you like to replace a random character with a random number? \n"
                       "(You may wish to skip this if your generatd password already has a number). (Y/N): ").lower()
        if number == "y":
           Range = len(Passphrase) - 1
           Char2 = random.randint(1, Range)
           num = random.randint(0, 9)
           Passphrase2 = ""
           i = 0
           while i <= Range:
               if i == Char or i != Char2:
                   Passphrase2 += Passphrase[i]
                   i += 1
               elif i == Char2:
                   Passphrase2 += str(num)
                   i += 1
           Passphrase = Passphrase2
        elif number == "n":
            inputValid = True
        else:
            print("That is not a valid answer")
            continue
        inputValid = True
print("""

Here is your passphrase, please write it down and keep it somewhere safe until 
you've memorised it, at which point you should dispose of the written version in a secure manner.

                        """,Passphrase.capitalize())



