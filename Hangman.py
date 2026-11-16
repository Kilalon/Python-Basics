import random

def stickman():
    print()
    print('*********')
    print(wrongs[0])
    print(wrongs[1])
    print(wrongs[2])
    print(wrongs[3])
    print('*********')

def the_word(name):
    global wrongs
    global mistake
    global correct
    global name_list

    stickman()

    
    for index in name_list:
            print(index, end=' ')


    print()
    print()

    letter_guess = str(input("Guess the letter: ")).lower()

    if letter_guess in name and letter_guess != '' and letter_guess not in name_list:
            print(f"Correct letter!! '{letter_guess}'")
            correct += 1
            print(f"You got {correct} words out of the {correct_letters}")
            letter_number = name.index(letter_guess)
            name_list[letter_number] = letter_guess
    
    elif letter_guess not in name or letter_guess == '':
           mistake += 1
           print("Wrong letter!")
           print(f"Mistake {mistake} out of 5!")

    match mistake:
          case 1:
                wrongs[0] = '|   O   |'
          case 2:
                wrongs[1] = '|   |   |'
          case 3:
                wrongs[1] = '| --|-- |'
          case 4:
                wrongs[2] = '|   |   |'
          case 5:
                wrongs[3] = "|  / |  |"


while True:

    names = ['lemon','flu','fire']
    name = random.choice(names)
    name_list = []
    mistake = 0
    correct = 0
    correct_letters = 0
    for letter in name:
        correct_letters += 1
        name_list.append(" _ ")
    wrongs=['|       |' , '|       |' , '|       |'  ,'|       |'] 
      
    while True:
        the_word(name)
        if mistake == 5:
            stickman()
            print("You Died!")
            print("Game over!!")
            break
        
        elif correct == correct_letters:
            print(f"You got the word {name} correct!")
            print("You win!!!")
            break

    play_again = input("Would you like to play again? (yes/no): ").lower()
    if play_again == 'no' and play_again != '':
        break

print("Thanks for Playing!")
print("Have a nice day!")