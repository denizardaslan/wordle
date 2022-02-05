import random
import time

def wordananalyzer(chosenWord,userInput):
    chosenWordlist = []
    userInputlist = []

    for i in chosenWord:
        chosenWordlist.append(i)
    for i in userInput:
        userInputlist.append(i)

    chosenWorddict = {
        0:chosenWordlist[0],
        1:chosenWordlist[1],
        2:chosenWordlist[2],
        3:chosenWordlist[3],
        4:chosenWordlist[4],}

    userInputdict = {
        0: userInputlist[0],
        1: userInputlist[1],
        2: userInputlist[2],
        3: userInputlist[3],
        4: userInputlist[4],
        }
    showlist = []
    alternativelist = []
    i = 0
    while i<5:
        if userInputlist[i] in chosenWordlist:
            alternativelist.append(userInputlist[i])
        else:
            pass
        if userInputdict[i] == chosenWorddict[i]:
            showlist.append(True)
            i += 1
        else:
            showlist.append(False)
            i += 1
    return showlist,chosenWordlist,alternativelist



def shower(finalList,chosenWordlist,otherlist):
    i=0
    lastlist = []
    while i<5:
        if finalList[i] == True:
            print(chosenWordlist[i],end=" ")
            time.sleep(1)
            lastlist.append(chosenWordlist[i])
            i+=1
        else:
            print("_",end=" ")
            time.sleep(1)
            i += 1
    resultSame = list(set(otherlist)^set(lastlist))
    print(f"    {resultSame} true but wrong place")

#reading wordlis
with open ("keywordlist.txt", "r", encoding="utf-8") as klist:
    for i in klist:
        string = i
wordlist = string.split(" ")

with open ("wordlist.txt", "r", encoding="utf-8") as wlist:
    for i in wlist:
        string = i
wordlist2 = string.split(" ")

#generating todays word
randomNumber = random.randint(0, 2315)
chosenWord = wordlist[randomNumber]
#print(chosenWord)

#console
i=0
showResult=[]
print("""
******* WORDLE in Python *******
How To Play:
You have 6 chances to find the given word.
After 6 chance, the program will be terminated.
.
v0.1
******* WORDLE in Python *******
""")
while i<6:
    userInput = input("\nEnter a 5 letter word: ")
    if userInput == chosenWord:
        for i in userInput:
            showResult.append(i)
        i=0
        while i<5:
            print(showResult[i], end=" ")
            time.sleep(1)
            i+=1
        print("\n*** True Guess! ***")
        break

    if len(userInput) == 5:
        userInput=userInput.lower()
    else:
        print("\nIt must be 5 letters!")
        continue

    if not userInput in wordlist2:
        print("There is no such word!")
        continue
    finalList, chosenWordlist, otherlist = wordananalyzer(chosenWord,userInput)
    shower(finalList,chosenWordlist,otherlist)
    i += 1
    print("\nRemaining Chance: ", 6-i)
print(f"Word was {chosenWord}.")
