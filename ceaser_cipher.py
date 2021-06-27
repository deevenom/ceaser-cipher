# program for the encoding and decoding
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v',
            'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
            'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z']
# importing art from another python file using import
import art_ceaser

print ( art_ceaser.logo )

direction = input ( "Type 'encode' to encrypt, type 'decode' to decrypt :\n" )
text = input ( "Type your message:\n" ).lower ()
shift = int ( input ( "Type the shift number:\n" ) )
 # if shift is more then the alphabets then we modules the shift and get reminder this helpsus to work in range of alphabets
shift = shift % 26
# creating a function for encoding
def encrypt(start_text, shift_amount):
    decoded_msg = ""
    for letters in start_text:
        if letters in alphabet:
            position = alphabet.index ( letters )
            new_position = position + shift_amount
            message = alphabet[new_position]
            decoded_msg += message
        else:
            decoded_msg += letters
    print ( f"your encoded msg is {decoded_msg}" )


def decrypt(plain_text, shift_amt) :
    encoded_msg = ""
    for letter in plain_text:
        if letter in alphabet: #if there is any other symbol number or special chracter this going to store them  and then appens them
            position = alphabet.index(letter)
            new_position = position - shift_amt
            message = alphabet[new_position]
            encoded_msg += message
        else:
            encoded_msg += letter
    print(f"your decoded message is {encoded_msg}" )
# caliling of function
if direction == "encode":
    encrypt( start_text=text, shift_amount=shift )
elif direction == "decode":
        decrypt(plain_text= text, shift_amt= shift )
   