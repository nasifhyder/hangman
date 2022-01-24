import random
from variables import words

keep_going = True
lives = 6
rand_int = random.randint(0, 62)
selected_word = (words[rand_int]).lower()
selected_word_list = []
watch_list = []


for i in selected_word:
    selected_word_list.append(i)
    watch_list.append("_")


def checker(word, gue):
    k = []
    f = 0
    for l in word:
        if l == gue:
            k.append(f)
        f += 1
    return k


while keep_going:
    print(f"{watch_list} lives: {lives}")
    guess = (input("Guess:")).lower()
    if guess in selected_word_list:
        indices = checker(selected_word_list, guess)
        for z in indices:
            watch_list[z] = guess

        if watch_list == selected_word_list:
            print("you win")
            keep_going = False

    else:
        lives -= 1

        if lives == 0:
            print("you lose")
            keep_going = False
