import string
import random
NUMDIGITS = 3
MAXGUESS = 10

def getSecretNum(numDigits):
# Returns a string that is numDigits long, made up of unique random digits.
  numbers = list(range(10))
  random.shuffle(numbers)
  secretNum = ''
  for i in range(numDigits):
    secretNum += str(numbers[i])
  return secretNum

def getClues(guess, secretNum):
# Returns a string with the pico, fermi, None clues to the user.
  if guess == secretNum:
    return 'You got it!'
  clue = []
  for i in range(len(guess)):
    if guess[i] == secretNum[i]:
      clue.append('Fermi')
    elif guess[i] in secretNum:
      clue.append('Pico')
  if len(clue) == 0:
      return 'None'
  return ' '.join(clue)

def isOnlyDigits(num):
# Returns True if num is a string made up only of digits. Otherwise returns False.
  if num == '':
    return False

  for i in num:
    if i not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
      return False
  return True

def playAgain():
# This function returns True if the player wants to play again, otherwise it returns False.
  play = raw_input("Do you want to play again? Yes or No?") 
  if play == "yes" or play == 'y':
    return True
  else:
    return False



print('I am thinking of a %s-digit number. Try to guess what it is.' % (NUMDIGITS))
print('Here are some clues:')
print('When I say:    That means:')
print('  Pico         One digit is correct but in the wrong position.')
print('  Fermi        One digit is correct and in the right position.')
print('  None       No digit is correct.')

while True:
  secretNum = getSecretNum(NUMDIGITS)
  print('I have thought up a number. You have %s guesses to get it.' % (MAXGUESS))
  numGuesses = 1
  while numGuesses <= MAXGUESS:
    guess=''
    while len(guess) != NUMDIGITS or not isOnlyDigits(guess):
      print 'Guess' + str(numGuesses)
      guess = raw_input("Guess Again")

    clue = getClues(guess, secretNum)
    print(clue)
    numGuesses += 1
    if guess == secretNum:
      break
    if numGuesses > MAXGUESS:
      print 'You ran out of guesses. The answer was ' + secretNum
  if not playAgain:
    break
 
import choose_word
from images import IMAGES
import random


# End of helper code
# -----------------------------------

def is_word_guessed(secret_word, letters_guessed):# es line me jab use ek letter guess karte hai or random secret word rahta hai
    '''
    secret_word: ek string word jo ki user ko guess karna hai
    letters_guessed: ek list hai, jisme wo letters hai jo ki user nai abhi tak guess kare hai
    returns: return True kare agar saare letters jo ki user ne guess kiye hai wo secret_word mai hai, warna no
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    # remove this return

    if secret_word == get_guessed_word(secret_word, letters_guessed):# es line me secret word se guess kiya hua word ko comper karta hai 
        return True# ager if condition true hota hai to return ture karta hai
    return False #ager if condition false hota hai to return false karta hai
    # Iss function ko test karne ke liye aap get_guessed_word("kindness", [k, n, d]) call kar sakte hai


def if_valid(user_input):#ye line  user se vaild input word ke liye hai
    '''
    if_valid function : check krwa rhe h ki user ne jo input dala h wo sahi h ya nhi.
    phale if condition : check kr rhe h ki user ne jo input dala h uska lenght 1 hai ya nhi, agar user_input ka
    lenght 1 se jayda h to loop continue kr de qki ek br mai ek letter  game mai dalana h.
    aur dusre if condition : user_input srif alphhabets hi dale h ya nhi yhe check krwa rhe h.
    '''

    if len(user_input) == 1 and user_input.isalpha():#user input ka length se comper karta hai ek se jada hai ya kam
        return True#jab if condition true hota hai to return true karta hai
    else:
        return False #nahi to return false karta hai
    # .isalpha() ek builtin funtion h jo check krta h ki input ya koi v data alphabets mai h ya nhi
def get_hint(secret_word, letters_guessed):#ye function hint ke liye hai

    letters_not_guessed = []#jo letter guess nahi kiya jata hai wo esme raha hai.
    
    index = 0#variable
    while (index < len(secret_word)):#ye secert word tak loop chalega
        letter = secret_word[index]#letter ye ek variable hai jisme secert word store hoga
        if letter not in letters_guessed:
            if letter not in letters_not_guessed:
                letters_not_guessed.append(letter)

        index += 1

    return random.choice(letters_not_guessed)
    




def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: ek string word jo ki user ko guess kar raha hai
    letters_guessed: ek list hai, jisme wo letters hai jo ki user nai abhi tak guess kare hai
    returns: ek string return karni hai jisme wo letters ho jo sahi guess huye ho and baki jagah underscore ho.
    eg agar secret_word = "kindness", letters_guessed = [k,n, s]
    to hum return karenge "k_n_n_ss"
    '''

    index = 0#variable_use loop
    guessed_word = ""
    while (index < len(secret_word)):
        if secret_word[index] in letters_guessed:
            guessed_word += secret_word[index]
        else:
            guessed_word += "_"
        index += 1
    
    return guessed_word


def get_available_letters(letters_guessed):#esme  all word ke avaiable letter hai jo user  guess karga
    '''
    letters_guessed: ek list hai, jisme wo letters hai jo ki user nai abhi tak guess kare hai
    returns: string, hame ye return karna hai ki kaun kaun se letters aapne nahi guess kare abhi tak
    eg agar letters_guessed = ['e', 'a'] hai to humme baki charecters return karne hai
    jo ki `bcdfghijklmnopqrstuvwxyz' ye hoga
    '''
    # FILL IN YOUR CODE HERE...
    all_letters = string.ascii_lowercase
    letters_left = " "
    for letters in all_letters: 
        if letters not in letters_guessed:
            letters_left += letters

    # FILL IN YOUR CODE HERE...
    # remove this return
    return letters_left

def hangman(secret_word):#yaha se hangman start hota hai
    '''
    secret_word: string, the secret word to guess.

    Hangman game yeh start karta hai:

    * Game ki shuruaat mei hi, user ko bata dete hai ki
      secret_word mei kitne letters hai

    * Har round mei user se ek letter guess karne ko bolte hai

    * Har guess ke baad user ko feedback do ki woh guess uss
      word mei hai ya nahi

    * Har round ke baar, user ko uska guess kiya hua partial word
      display karo, aur underscore use kar kar woh letters bhi dikhao
      jo user ne abhi tak guess nahi kiye hai

    '''
    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is " + str(len(secret_word)) + " letters long."
    print "In Which difficulty level you want to play HANGMAN GAME?  HARD, MEDIUM, OR EASY"
    user_difficulty_choice = raw_input("apke pas three level hai. Hard/hard level khalne ke liye hard likhiye , medium level khelne ke liye medium likhye aur easy khalna hai to easy likhiye:-" )
    if user_difficulty_choice == "HARD" or user_difficulty_choice == "hard":
        print "You have choosen hard level... All the very best!!!"
        remaining_lives = total_lives= 4
        images_selection_list_indices = [1, 3, 5, 7]
    elif user_difficulty_choice == "MEDIUM" or user_difficulty_choice == "medium":
        print "you have choosen medium level... All the best!!!"
        remaining_lives = total_lives= 6
        images_selection_list_indices = [0, 2,  4, 6]
    elif user_difficulty_choice == "EASY" or user_difficulty_choice == "easy":
        print "You have choosen easy level... May you will!!!"
        remaining_lives = total_lives = 8
        images_selection_list_indices = [0, 1, 2, 3, 4, 5, 6, 7]
    else:
        print "You entered invalid option... So just start with easy mode!!!"
        print "You have choosen easy level... May you will!!!"
        remaining_lives = total_lives=8
        images_selection_list_indices = [0, 1, 2, 3, 4, 5, 6, 7]



    letters_guessed = []
    
    available_letters = get_available_letters(letters_guessed)
    print "Available letters: " + available_letters

    while remaining_lives != 0:
        guess = raw_input("Please guess a letter: ")
        if guess == "hint":
            letter = get_hint(secret_word, letters_guessed)
        
        else:
            letter = guess.lower()

            if (not if_valid(letter)):
                print "Invalid Input! Make sure you are only entering single alphabet at a time."
                continue

        if letter in secret_word:
            letters_guessed.append(letter)

            print "Good guess: " + get_guessed_word(secret_word, letters_guessed)
            print ""

            if is_word_guessed(secret_word, letters_guessed) == True:
                print " * * Congratulations, you won! * * "
                print ""
                break

        else:
            print "Oops! That letter is not in my word: " + get_guessed_word(secret_word, letters_guessed)
            letters_guessed.append(letter)
            
            
            print IMAGES[images_selection_list_indices[total_lives-remaining_lives]] ## <-- CHANGES HERE

            available_letters = get_available_letters(letters_guessed)
            print "Available letters: " + available_letters
            remaining_lives = remaining_lives-1
            print "Remaining lives = " , remaining_lives
            print "Better luck next time."
            print ""
    print "SORRY, you have lose this game!"
    print "The letter was " +  secret_word
    


   
# Load the list of words into the variable wordlist
# So that it can be accessed from anywhere in the program
secret_word = choose_word()
hangman(secret_word)