import random


encrypts = {}
chars="1234567890abcdefghijklmnopqrstuvABCDEFGHIJKLMNOPQRSTUV!@#$%^&*-_"
is_running = True

action = input("Would you like to encrypte or decrypte?: ").lower()

while is_running:
    match action:

        case 'encrypte':
            word = input("Enter the message you would like to encrypte: ")
            encryption=''
            for letter in word:
                encryption += random.choice(chars)
            encrypts.update({encryption:word})
            print(f"Your word is: {word}")
            print(f"The encryption is: {encryption}")

        case 'decrypte':
            try:
                decryption = input("Enter the message you would like to decrypte: ")
                word = encrypts.get(decryption)
                print(f"The encrypted message is: {decryption}")
                print(f"The decrypted word is: {word}")
            except:
                print("What you entered isn't found!")

        case 'show dict':
            for x, y in encrypts.items():
                print(x,' : ', y)

    action = input("Would you like to encrypte or decrypte or exit?: ").lower()
    if action == 'exit':
        is_running = False

print("have a nice day")