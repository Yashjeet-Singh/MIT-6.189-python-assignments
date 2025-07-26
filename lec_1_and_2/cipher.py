# -*- coding: cp1252 -*-
# Yashjeet Singh
# June 1st, 2025
# cipher.py

'''
This program takes a sentence and a shift value from the user, then applies the
Caesar Cipher to encrypt each alphabetical character by shifting it forward in
the alphabet, wrapping around as needed. Non-letter characters remain unchanged.
The result is printed as the encoded message.
'''

# Asks the user to enter the phrase to encode and stores it in the variable named
# phrase_to_encode
phrase_to_encode = input("Enter sentence to encrypt: ")

# Asks the user to enter shift value for encrypting the message
shift_value = int(input("Enter shift value: "))

# Initialized an empty variable encoded_phrase
encoded_phrase = ''

# A for loop to iterate over and modify the letters of simple phrase to encoded phrase
for char in phrase_to_encode:
    # getting the ascii code value of the char in the phrase
    ascii_code = ord(char)

    # checking where the ascii value is in the table and performing the required operation
    if 96 < ascii_code < 123 :
        # Main crux of the problem
        ascii_code = (ascii_code + shift_value - 97)%26 + 97
    elif 64 < ascii_code < 91:
        # Main crux of the problem
        ascii_code = (ascii_code + shift_value - 65)%26 + 65
    else:
        # Written just for the clarity
        ascii_code = ascii_code

    # An encoded phrase getting encoded each time through the loop
    encoded_phrase = encoded_phrase + chr(ascii_code)

# printing the encoded phrase
print ("The encoded phrase is:", encoded_phrase)


##letter = 'a'
### converts a letter to ascii code 
##ascii_code = ord(letter) 
### converts ascii code to a letter 
##letter_res = chr(ascii_code) 
##print ascii_code, letter_res
