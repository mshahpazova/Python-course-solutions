def inception():
    word = input()
    config = list(len(word) * '-')
    count = 0
    POSSIBLE_TRIES = 10
    print(config)
    wrong_tries = 0
    guessed_letters = 0
    while wrong_tries < POSSIBLE_TRIES:
        print(POSSIBLE_TRIES)
        letter_try = input()
        print(letter_try)
        if (letter_try not in word):
            print("not in word")
            wrong_tries += 1
        else:
            for index, letter in enumerate(word):
                if (letter_try == letter):
                    config[index] = letter
                    guessed_letters += 1
        print(''.join(config))
        if guessed_letters == len(word):
          print("Congrats you win")



inception()

