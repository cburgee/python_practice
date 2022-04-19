BASE = ord("a")
MAX = ord("z") - ord("a")
A = ord("a")
Z = ord("z")
repeat = True


def decrypt(str, shift):
    return encrypt(str, -shift)


def encrypt(str, shift):
    letter = 0
    shifted_str = ""
    for l in str:
        letter = ord(l) + shift
        if letter > Z:
            letter -= 26
        if letter < A:
            letter += 26
        shifted_str += chr(letter)
    return shifted_str


while repeat == True:
    encrpyt_decrypt = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")
    message_to_encrypt = input("Type your message: \n")
    shift_amount = int(input("Type the shift number: \n"))
    if encrpyt_decrypt == "encode":
        print(encrypt(message_to_encrypt, shift_amount))
    else:
        print(decrypt(message_to_encrypt, shift_amount))
    go_again = input("Would you like to go again? 'yes' or 'no' \n")
    if go_again == "no" or go_again != "yes":
        repeat = False
