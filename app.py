import random

with open('words.txt', 'r') as wordfile:
    texts = wordfile.readlines()
    textsnew = [text.replace('\n', '') for text in texts]

CORRECT_WORD = random.choice(textsnew)
count = 0

while count < 3:
    user_guess = input("Enter your guess: ").lower()

    correct_letters = {letter for correct, letter in zip(CORRECT_WORD, user_guess) if letter == correct}
    misplaced_words = set(user_guess) & set(CORRECT_WORD) - correct_letters
    wrong_words = set(user_guess) - set(CORRECT_WORD)

    count += 1

    print(f"Correct letters: {correct_letters}")
    print(f"Misplace: {misplaced_words}")
    print(f"wrong WOrds: {wrong_words}")

    if len(wrong_words) == 0:
        print("YOU WIN THE GAME!!!!!! ")
        break

if user_guess != CORRECT_WORD:
    print("The correct word was: ", CORRECT_WORD)