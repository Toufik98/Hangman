from random import choice

print("H A N G M A N")
choice_ = input('Type "play" to play the game, "exit" to quit:')
words_list = ("python", "java", "kotlin", "javascript")
right_word = choice(words_list)
mask_word = '-' * len(right_word)
lowercase_letter = 'abcdefghijklmnopqrstuvwxyz'
tries = 8
win = False
inputed_letters = []

if choice_ == 'play':
    while tries > 0:
        print()
        print(mask_word)
        letter = input("Input a letter:")
        inputed_letters.append(letter)
        if len(letter) == 1:
            if letter in lowercase_letter:
                if letter in right_word:
                    if (mask_word[right_word.find(letter)] != '-'):
                        print('You already typed this letter')

                    else:
                        for i in range(len(right_word)):
                            if letter == right_word[i]:
                                mask_word = mask_word[:i] + letter + mask_word[i + 1:]
                        if (mask_word == right_word):
                            tries = 0
                            win = True
                else:
                    if inputed_letters.count(letter) > 1:
                        print('You already typed this letter')
                    else:
                        print("No such letter in the word")
                        tries -= 1
            else:
                print("It is not an ASCII lowercase letter")
        else:
            print("You should input a single letter")
    if win:
        print()
        print(right_word)
        print('You guess the word!')
        print('You survived!')
    else:
        print("You are hanged!")
else :
    exit()
