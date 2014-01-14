import random

deadcount = 7
allWords = "rabbit house skirt stone wing banana tree butter chopsticks \
glass weight mountain book girl idea path salt nose paper river angel \
cloud engine garden sock twine seed slime keyboard shovel pain wire \
electricity locust dandruff figure water soap marshmallow asphalt death \
ash mist gold comb oil hammer barn hair couch card "
listOfWords = allWords.split()
word = random.choice(listOfWords)

currentList = ["_"] *len(word)
print " ".join(currentList)
guessesList = []

#remove case-sensitivity
#add category hint - make longer listOfWords

while "_" in currentList and deadcount > 0:
    guess = raw_input()
    if guess == word:
        print "YOU WIN!"
        break
    #add some way of validifying guess (i.e. no non-letters)
    if guess in guessesList:
        print "You already guessed this."
    elif guess in word:
        guessesList.append(guess)
        for i in range(0, len(word)):
            if guess == word[i]:
                currentList[i] = guess
        print " ".join(currentList)
    else:
        guessesList.append(guess)
        deadcount = deadcount - 1
        if deadcount == 1:
            print "1 try left."
        elif deadcount > 1:
            print str(deadcount) + " tries left."
        

if "_" not in currentList:
    print "YOU WIN!"
if deadcount == 0:
    print "YOU LOSE. The answer was " + word.upper() + "."
            
    
