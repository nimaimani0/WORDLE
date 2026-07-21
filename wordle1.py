#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 20:00:06 2026

@author: nima
"""

import random

with open("words.txt", "r") as file:
    words = [word.strip().lower() for word in file]

play = True

while play:

    while True:
        try:
            length = int(input(
                "\nwellcome!\nchoose word length (3 / 4 / 5 / 6): "
            ))

            if length in [3, 4, 5, 6]:
                break
            else:
                print("please enter only 3, 4, 5 or 6.")

        except ValueError:
            print("please enter a number:).")

    filtered_words = [word for word in words if len(word) == length]
    secret_word = random.choice(filtered_words)

    for attempt in range(6):

        while True:

            guess = input(
                f"attempt {attempt+1}/6 - enter a {length}-letter word: "
            ).lower()

            if len(guess) != length:
                print(f"word must be exactly {length} letters.")
                continue

            if guess not in filtered_words:
                print("This word is not in the dictionary.")
                continue

            break

        for i in range(length):
            if guess[i] == secret_word[i]:
                print("🟩", end="")
            elif guess[i] in secret_word:
                print("🟨", end="")
            else:
                print("⬜", end="")
        print()

        if guess == secret_word:
            print(" congratulations! You guessed the word\n you won.")
            break

    else:
        print("game Over!")
        print("the word was:", secret_word)

    while True:

        print("\n=====GAME MENU =====")
        print("1. play again :) ")
        print("2. exit :( ")

        choice = input("choose: ")

        if choice == "1":
            break

        elif choice == "2":
            print("thanks for playing ❤️")
            play = False
            break

        else:
            print("invalid choice :/ .")