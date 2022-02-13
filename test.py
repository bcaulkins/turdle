from ast import And
from cmath import log10
from pickle import FALSE, TRUE
from colorama import Fore, Back, Style


word = 'story'

print(word)

word_list = list(word)

print(word_list)

l1 = word_list[0]
l2 = word_list[1]
l3 = word_list[2]
l4 = word_list[3]
l5 = word_list[4]


print(l1)
print(l2)
print(l3)
print(l4)
print(l5)

guess=input()

guess_list=list(guess)

print(guess_list[0])
print(guess_list[1])
print(guess_list[2])
print(guess_list[3])
print(guess_list[4])

if guess_list[0] == l1:
    print('This is the first letter of the word.')
    print('\033[32m'+ guess_list[0]+Style.RESET_ALL)
    letter1 = str('\033[32m'+ guess_list[0]+Style.RESET_ALL)
elif guess_list[0] not in word_list:
    print('Letter, '+ str(guess_list[0])+ ', is not in the word')
    print('\033[31m'+guess_list[0]+Style.RESET_ALL)
    letter1 = str('\033[31m'+guess_list[0]+Style.RESET_ALL)
elif guess_list[0] in word_list and guess_list[0] != l1:
    print('The letter is in the word, but not in the right place.')
    print('\033[33m'+guess_list[0]+Style.RESET_ALL)
    letter1 = str('\033[33m'+guess_list[0]+Style.RESET_ALL)

if guess_list[1] == l2:
    print('This is the second letter of the word.')
    print('\033[32m'+ guess_list[1]+Style.RESET_ALL)
    letter2 = str('\033[32m'+ guess_list[1]+Style.RESET_ALL)
elif guess_list[1] not in word_list:
    print('Letter, '+ str(guess_list[1])+ ', is not in the word')
    print('\033[31m'+guess_list[1]+Style.RESET_ALL)
    letter2 = str('\033[31m'+guess_list[1]+Style.RESET_ALL)
elif guess_list[1] in word_list and guess_list[1] != l2:
    print('The letter is in the word, but not in the right place.')
    print('\033[33m'+guess_list[1]+Style.RESET_ALL)
    letter2 = str('\033[33m'+guess_list[1]+Style.RESET_ALL)

if guess_list[2] == l3:
    print('This is the third letter of the word.')
    print('\033[32m'+ guess_list[2]+Style.RESET_ALL)
    letter3 = str('\033[32m'+ guess_list[2]+Style.RESET_ALL)
elif guess_list[2] not in word_list:
    print('Letter, '+ str(guess_list[2])+ ', is not in the word')
    print('\033[31m'+guess_list[2]+Style.RESET_ALL)
    letter3 = str('\033[31m'+guess_list[2]+Style.RESET_ALL)
elif guess_list[2] in word_list and guess_list[2] != l3:
    print('The letter is in the word, but not in the right place.')
    print('\033[33m'+guess_list[2]+Style.RESET_ALL)
    letter3 = str('\033[33m'+guess_list[2]+Style.RESET_ALL)

if guess_list[3] == l4:
    print('This is the fourth letter of the word.')
    print('\033[32m'+ guess_list[3]+Style.RESET_ALL)
    letter4 = str('\033[32m'+ guess_list[3]+Style.RESET_ALL)
elif guess_list[3] not in word_list:
    print('Letter, '+ str(guess_list[3])+ ', is not in the word')
    print('\033[31m'+guess_list[3]+Style.RESET_ALL)
    letter4 = str('\033[31m'+guess_list[3]+Style.RESET_ALL)
elif guess_list[3] in word_list and guess_list[3] != l4:
    print('The letter is in the word, but not in the right place.')
    print('\033[33m'+guess_list[3]+Style.RESET_ALL)
    letter4 = str('\033[33m'+guess_list[3]+Style.RESET_ALL)

if guess_list[4] == l5:
    print('This is the fifth letter of the word.')
    print('\033[32m'+ guess_list[4]+Style.RESET_ALL)
    letter5 = str('\033[32m'+ guess_list[4]+Style.RESET_ALL)
elif guess_list[4] not in word_list:
    print('Letter, '+ str(guess_list[4])+ ', is not in the word')
    print('\033[31m'+guess_list[4]+Style.RESET_ALL)
    letter5 = str('\033[31m'+guess_list[4]+Style.RESET_ALL)
elif guess_list[4] in word_list and guess_list[4] != l5:
    print('The letter is in the word, but not in the right place.')
    print('\033[33m'+guess_list[4]+Style.RESET_ALL)
    letter5 = str('\033[33m'+guess_list[4]+Style.RESET_ALL)

print(letter1+letter2+letter3+letter4+letter5)

