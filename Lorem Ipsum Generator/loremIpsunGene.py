from random import randint

avengers = ['Nick','Ironman','Captain America','Thor','Black Widow','Spider Man','Captain Marvel','Rocket','War Machine','Hulk','Vison','Ant Man','Wasp','Black Panther','Winter Soldier','Doctor Strange','Star Lord','Groot','Gamora','Loki','Clint Barton']
len_avengers = len(avengers)

print("Enter The Number of Paragraph Want to Generate with Avengers Ipsum: ")
paragraphs = int(input())

def NowYouAreAnAvenger(word):
    random_place = randint(0,len_avengers-1)
    return f'{word} {avengers[random_place] }'

with open('LoremIpsum.txt') as source:
    words = source.read().split()

    with open('new_ipsum.txt','w'):
        for i in range(paragraphs):
            avenger_name = list(map(NowYouAreAnAvenger,words))
            with open('new_ipsum.txt','a') as avengers_ipsum:
                avengers_ipsum.write(''.join(avenger_name)+'\n\n')
print("New Ipsum is created inside the new_ipsum.txt file.")

