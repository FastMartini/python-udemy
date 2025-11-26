from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    
    if encode_or_decode == "decode":
        shift_amount *= -1
    
    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
        else:
            letter_index = alphabet.index(letter)
            new_letter_index = shift_amount + letter_index
            output_text += alphabet[new_letter_index]
            
    if encode_or_decode not in ("encode", "decode"):
        print("ERROR")
    else:
        print(f"Here is the {encode_or_decode} result: {output_text}")



direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

end_game = False

caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

while not end_game:
    question = input(f"Do you want to go again? Yes/No\n").lower()
    if question == "yes":
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
    else:
        end_game = True
        print("Goodbye!")