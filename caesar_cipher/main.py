alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

encrypted_text = ""
decrypted_text = ""

def encrypt(text, shift):
    global encrypted_text
    for character in text:
        if character in alphabet:
            position = alphabet.index(character)
            new_character = alphabet[(position + shift) % 26]
            encrypted_text += new_character
        else:
            encrypted_text += character
    print(encrypted_text)

def decrypt(text, shift):
    global decrypted_text
    for character in text:
        if character in alphabet:
            position = alphabet.index(character)
            new_character = alphabet[(position - shift) % 26]
            decrypted_text += new_character
        else:
            decrypted_text += character
    print(decrypted_text)

if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)
else:
    print("invalid input")
