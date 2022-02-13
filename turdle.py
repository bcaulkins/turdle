from mimetypes import init
import os, random
from time import sleep
from colorama import Fore, Back, Style
from collections import Counter

init()

def screen_clear():
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')

#sets path to list of words for the game.
filepath = 'turdles.txt'

words = [line.strip() for line in open(filepath)]

#picks a random word from the list and sets that word as the value of the variable turdle.
turdle = random.choice(words)
failed = str('The TURDLE for the day was: ' + turdle.upper() + '! Have a nice day and feel free to try again!')
print(turdle)

#takes each letter of the random word and puts it into an array.
turdle_turdle = list(turdle)

l1=turdle_turdle[0]
l2=turdle_turdle[1]
l3=turdle_turdle[2]
l4=turdle_turdle[3]
l5=turdle_turdle[4]

print(turdle_turdle)

print ('Welcome to TURDLE a WORDLE clone!\n')
print('HOW TO PLAY\n')
print ('Guess the TURDLE in six tries.\n')
print('After each guess, the color of the LETTER will change to show how close your guess was to the word.\n')
print('Examples:\n')
print(Fore.GREEN+'W'+Style.RESET_ALL+'EARY\n')
print('The letter W is in the word and in the correct spot.\n')
print('P'+Fore.YELLOW+'I'+Style.RESET_ALL+'LLS\n')
print('The letter I is in the word but in the wrong spot.\n')
print('VAG'+Fore.RED+'U'+Style.RESET_ALL+'E')
print('The letter U is not in the word in any spot.\n')
print ('Let\'s get started!')

guesses = 1

word_guess1 = ''
word_guess2 = ''
word_guess3 = ''
word_guess4 = ''
word_guess5 = ''

letter_guess1 = ''
letter_guess2 = ''
letter_guess3 = ''
letter_guess4 = ''
letter_guess5 = ''

while guesses < 7:
    #print ('_ _ _ _ _')
    guess_1 = input ('Guess ' +str(guesses)+':')
    if len(guess_1) != 5:
        #screen_clear()
        print('Word guess is not the correct length. Try again.')        
    else:
        guess_1a = list(guess_1)
        if guess_1 == turdle:
            if guesses == 1:
                print('Congrats! You guessed the TURDLE in ' + str(guesses) + ' guess! Have a nice day!')
                sleep(10)
                quit()
            else:
                #print(letter_guess1+letter_guess2+letter_guess3+letter_guess4+letter_guess5)
                print('Congrats! You guessed the TURDLE in ' +str(guesses) + ' guesses! Have a nice day!')
                sleep(10)
                quit()
        #screen_clear()
#--------------------------------------------------------------------------------        
        if guess_1a[0]==l1:
            letter_guess1=str('\033[32m'+ guess_1a[0]+Style.RESET_ALL) #green letter
        
        elif guess_1a[0] in turdle_turdle and guess_1a[0] != l1:
            letter_guess1=str('\033[33m'+ guess_1a[0]+Style.RESET_ALL) #yellow letter

        elif guess_1a[0] not in turdle_turdle:
            letter_guess1=str('\033[31m'+ guess_1a[0]+Style.RESET_ALL) #white letter
#--------------------------------------------------------------------------------
        if guess_1a[1]==l2:
            letter_guess2=str('\033[32m'+ guess_1a[1]+Style.RESET_ALL) #green letter       
       
        elif guess_1a[1] in turdle_turdle and guess_1a[1]!=l2:
            letter_guess2=str('\033[33m'+ guess_1a[1]+Style.RESET_ALL) #yellow letter

        elif guess_1a[1] not in turdle_turdle:
            letter_guess2 = str('\033[31m'+guess_1a[1]+Style.RESET_ALL) #white letter
#--------------------------------------------------------------------------------
        if guess_1a[2]==l3:
            letter_guess3=str('\033[32m'+ guess_1a[2]+Style.RESET_ALL) #green letter
        
        elif guess_1a[2] in turdle_turdle and guess_1a[2]!=l3:
            letter_guess3=str('\033[33m'+ guess_1a[2]+Style.RESET_ALL) #yellow letter

        elif guess_1a[2] not in turdle_turdle:
            letter_guess3 = str('\033[31m'+guess_1a[2]+Style.RESET_ALL) #white letter
#--------------------------------------------------------------------------------
        if guess_1a[3]==l4:
            letter_guess4=str('\033[32m'+ guess_1a[3]+Style.RESET_ALL) #green letter
        
        elif guess_1a[3] in turdle_turdle and guess_1a[3]!=l4:
            letter_guess4=str('\033[33m'+ guess_1a[3]+Style.RESET_ALL) #yellow letter

        elif guess_1a[3] not in turdle_turdle:
            letter_guess4 = str('\033[31m'+guess_1a[3]+Style.RESET_ALL) #white letter
#--------------------------------------------------------------------------------
        if guess_1a[4]==l5:
            letter_guess5=str('\033[32m'+ guess_1a[4]+Style.RESET_ALL) #green letter
        
        elif guess_1a[4] in turdle_turdle and guess_1a[4]!=l5:
            letter_guess5=str('\033[33m'+ guess_1a[4]+Style.RESET_ALL) #yellow letter

        elif guess_1a[4] not in turdle_turdle:
            letter_guess5 = str('\033[31m'+guess_1a[4]+Style.RESET_ALL) #white letter
#--------------------------------------------------------------------------------
        print(letter_guess1+letter_guess2+letter_guess3+letter_guess4+letter_guess5)
        guesses=guesses+1
        

        
print(failed)

sleep(10)
quit()