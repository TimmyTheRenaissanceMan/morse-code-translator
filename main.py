import pandas as pd


# The function 1. loads Morse 2. expects user to choose whether to encode/decode
# 3. expects user to input a text or a path to a text file
def morse_translator():
    morse = pd.read_csv("./resources/morse_code.csv", sep="%;", engine="python")
    morse["CHAR"][26] = " "
    encode_or_decode = input("Press E to encode or D to decode: ").upper()
    if encode_or_decode == "E" or encode_or_decode == "D":
        request = input("Please, enter a text or a relative path to a .txt file: ")
        try:
            with open(request, "r") as file:
                text = file.read().upper()
                print("Reading..")
        except:
            print("The path was not found.\nThe input will be treated as plain text.")
            text = request.upper()
        finally:
            if encode_or_decode == "D":
                decode(text, morse)
            else:
                encode(text, morse)
    else:
        morse_translator()


# Identify a character or set of characters that are used to separate encoded words
def identify_separator(sample):
    separator = ""
    is_on = True
    for i in sample:
        if is_on:
            if i != "." and i != "-":
                separator = separator + i
            else:
                if separator != "":
                    return separator


# Initialize decoding of the input. The function expects encoded text and morse alphabet
def decode(text, morse_alphabet):
    decoded_text = ""
    separator = identify_separator(text[0:25])
    text_array = text.split(separator)
    for letter in text_array:
        try:
            if letter == "\n":
                decoded_letter = "\n"
            else:
                decoded_letter = morse_alphabet[morse_alphabet["CODE"] == letter]["CHAR"].values[0]
        except:
            decoded_letter = "[ERR]"
        finally:
            print(letter)
            decoded_text = decoded_text + decoded_letter
    with open("output/decoded.txt", "w", encoding="utf-8") as output_file:
        output_file.write(decoded_text)


# initialize encoding of the input. The function expects raw text and morse alphabet
def encode(text, morse_alphabet):
    encoded_text = ""
    separator = input(f'The default separator is [SPACE]'
                      f'Please enter a custom separator or press ENTER to continue: ')
    if not separator:
        separator = " "
    for letter in text:
        try:
            if letter == "\n":
                encoded_letter = "\n"
            else:
                encoded_letter = morse_alphabet[morse_alphabet["CHAR"] == letter]["CODE"].values[0]
        except:
            encoded_letter = "[ERR]"
        finally:
            encoded_text = encoded_text + encoded_letter + separator
    with open("output/encoded.txt", "w", encoding="utf-8") as output_file:
        output_file.write(encoded_text)


morse_translator()
