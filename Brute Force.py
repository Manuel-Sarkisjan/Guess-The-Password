import random
import pyautogui
import time

character = "0123456789abcdefghijklmnopqrstuvwxyz"
character_list = list(character)

password = pyautogui.password("Enter password here:").lower()  # Convert to lowercase

start_time = time.time()
guess_password = " "
attempts = 0

while guess_password != password:
    guess_password = "".join(random.choices(character_list, k=len(password))).lower()  # Convert to lowercase
    attempts += 1

    print("||||||" + str(guess_password) + "|||||")

    if guess_password == password:
        end_time = time.time()
        elapsed_time = end_time - start_time
        print("Your password is:", guess_password)
        print(f"Cracked in {attempts} attempts and {elapsed_time:.2f} seconds.")
        break