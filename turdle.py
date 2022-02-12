import os, random
from time import sleep

def screen_clear():
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')

#sets path to list of words for the game.
filepath = 'turdles.txt'
#read_turdles = open(filepath, 'r')
#turdles = read_turdles.readline()

words = [line.strip() for line in open(filepath)]
#print(random.choice(words))

#picks a random word from the list and sets that word as the value of the variable turdle.
turdle = random.choice(words)
failed = str('The TURDLE for the day was: ' + turdle.upper() + '! Have a nice day and feel free to try again!')
#print(failed)

#takes each letter of the random word and puts it into an array.
turdle_turdle = list(turdle)

l1=turdle_turdle[0]
l2=turdle_turdle[1]
l3=turdle_turdle[2]
l4=turdle_turdle[3]
l5=turdle_turdle[4]

#print(l5)



#print(turdle_turdle)

print ('Welcome to TURDLE a WORDLE clone!')
print ('You have 6 attempts to guess the word.')
print ('Let\'s get started!')

guesses = 1
while guesses < 7:
    print ('_ _ _ _ _')
    guess_1 = input ('Guess ' +str(guesses)+':')
    if len(guess_1) != 5:
        screen_clear()
        print('Word guess is not the correct length. Try again.')        
    else:
        guess_1a = list(guess_1)
        if guess_1 == turdle:
            if guesses == 1:
                print('Congrats! You guessed the TURDLE in ' + str(guesses) + ' guess ! Have a nice day!')
                sleep(10)
                quit()
            else:
                print('Congrats! You guessed the TURDLE in ' +str(guesses) + ' guesses ! Have a nice day!')
                sleep(10)
                quit()
        screen_clear()
        if guess_1a[0]==l1:
            print(guess_1a[0])
        else: print('_')
        if guess_1a[1]==l2:
            print(guess_1a[1])
        else: print('_')
        if guess_1a[2]==l3:
            print(guess_1a[2])
        else: print('_')
        if guess_1a[3]==l4:
            print(guess_1a[3])
        else: print('_')
        if guess_1a[4]==l5:
            print(guess_1a[4])
        else: print('_')
        guesses=guesses+1
        
print(failed)
#print('Game Over. Please Try Again.')
sleep(10)
quit()
#print (guess_1)

#sleep (10)

#read_turdles.close()