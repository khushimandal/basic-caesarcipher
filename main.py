alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(text, shift):
    newtext = ""
    for char in text:
        if char in alphabet:
            index = alphabet.index(char)
            if index + shift > 25:
                index = index + shift - 26
            else:
                index = index + shift
            newtext += alphabet[index]
        else:
            newtext += char
    print(f"Encoded text is {newtext}")

def decrypt(text, shift):
    plaintext = ""
    for char in text:
        if char in alphabet:
            index = alphabet.index(char)
            if index - shift < 0:
                index = index - shift + 26
            else:
                index = index - shift
            plaintext += alphabet[index]
        else:
            plaintext += char
    print(f"Decoded text is {plaintext}")


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)
else:
    print("Invalid choice. Please type 'encode' or 'decode'.")
