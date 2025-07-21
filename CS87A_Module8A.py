'''
created 7/20/25

sample cypher/decypher function

@author Oscar Chaltiel 
'''

import random

shift_key = 0  # store the random shift globally 

def make_key():
    # pick a random shift between 1 and 26 and store it in shift_key.
    global shift_key
    shift_key = random.randint(1, 26)
    return shift_key

def shift_char(ch, shift):

    # if character is uppercase A–Z
    if ch.isupper():
        # Get its position in alphabet (A=0, B=1, … Z=25)
        position = ord(ch) - ord('A')
        new_position = (position + shift) % 26
        # Convert back to a character
        new_char = chr(ord('A') + new_position)
        return new_char

    # if character is lowercase a–z
    elif ch.islower():
        # Get its position in alphabet (a=0, b=1, … z=25)
        position = ord(ch) - ord('a')
        new_position = (position + shift) % 26
        # Convert back to a character
        new_char = chr(ord('a') + new_position)
        return new_char

    # if it's not a letter leave it alone
    else:
        return ch

def cipher(text):
    global shift_key
    make_key()  # pick a random shift
    result = ""
    for ch in text:
        result += shift_char(ch, shift_key)
    return result

def decipher(text):
    global shift_key
    result = ""
    for ch in text:
        result += shift_char(ch, -shift_key)
    return result

def main():
    user_text = input("Type a message to encode: ")

    encoded_text = cipher(user_text)
    print(f"Here is your encoded message: {encoded_text}")

    decoded_text = decipher(encoded_text)
    print(f"Here is your decoded message: {decoded_text}")

    if decoded_text == user_text:
        print("Cipher is working properly!")
    else:
        print("Whoops, cipher is broken.")

main()