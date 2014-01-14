import random

deadcount = 7
all_words = "rabbit house skirt stone wing banana tree butter chopsticks \
glass weight mountain book girl idea path salt nose paper river angel \
cloud engine garden sock twine seed slime keyboard shovel pain wire \
electricity locust dandruff figure water soap marshmallow asphalt death \
ash mist gold comb oil hammer barn hair couch card "
list_of_words = all_words.split()
word = random.choice(list_of_words)

current_list = ["_"] * len(word)
print " ".join(current_list)
guesses_list = []

#remove case-sensitivity
#add category hint - make longer list_of_words

while "_" in current_list and deadcount > 0:
    guess = raw_input()
    if guess == word:
        print "YOU WIN!"
        break
    #add some way of validifying guess (i.e. no non-letters)
    if guess in guesses_list:
        print "You already guessed this."
    elif guess in word:
        guesses_list.append(guess)
        for i in range(0, len(word)):
            if guess == word[i]:
                current_list[i] = guess
        print " ".join(current_list)
    else:
        guesses_list.append(guess)
        deadcount = deadcount - 1
        if deadcount == 1:
            print "1 try left."
        elif deadcount > 1:
            print str(deadcount) + " tries left."
        

if "_" not in current_list:
    print "YOU WIN!"
if deadcount == 0:
    print "YOU LOSE. The answer was " + word.upper() + "."
            
    
