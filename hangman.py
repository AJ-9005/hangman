import random
fh=open("words.txt","r")
words=list(map(str.strip, fh.readlines()))
fh.close()
def getaword(wordlist):
    global word
    word=random.choice(wordlist)
getaword(words)
hidlis=[]
usedlets=[]
for _ in range(0,len(word)):
    hidlis.append("-")
def hidwordupdater(key):
    for i in range(0,len(word)):
        if word[i]==key:
            hidlis[i]=key
def game():
    count=0
    lives=6
    while lives>0 and formedword(hidlis)!=word:
        print(f"Lives left:{lives}")
        print("letters used=",usedlets)
        for i in hidlis:
            print(i,end="")
        z=input("\nGuess a letter:")
        if z in word:
            usedlets.append(z)
            hidwordupdater(z)
            print("Correct letter guessed")
            count+=1
        else:
            print("Wrong letter guessed")
            usedlets.append(z)
            lives-=1
            count+=1
    if formedword(hidlis)==word:
        print(f"Word found! It was {word}!\n It took you {count} tries!")
    elif lives==0:
        print(f"You failed u loser!It was {word}!")
def formedword(lis):
    str1=""
    for i in lis:
        str1+=i
    return str1
game()