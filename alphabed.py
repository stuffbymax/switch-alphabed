def shift_letter(letter, shift):
    if letter.isalpha():
        # Handle uppercase and lowercase letters
        base = ord('A') if letter.isupper() else ord('a')
        return chr((ord(letter) - base + shift) % 26 + base)
    return letter

def encode_message(message, shift):
    return ''.join(shift_letter(char, shift) for char in message)

def decode_message(encoded_message, shift):
    # Decoding is the reverse of encoding, so we use -shift
    return encode_message(encoded_message, -shift)

def main():
    print("Welcome to the Encoder/Decoder App!")
    while True:
        choice = input("Would you like to (E)ncode, (D)ecode, or (Q)uit? ").lower()
        if choice == 'e':
            message = input("Enter the message to encode: ")
            shift = int(input("Enter the shift value (1-25): "))
            encoded_message = encode_message(message, shift)
            print(f"Encoded Message: {encoded_message}")
        elif choice == 'd':
            encoded_message = input("Enter the message to decode: ")
            shift = int(input("Enter the shift value (1-25): "))
            decoded_message = decode_message(encoded_message, shift)
            
            print(f"Decoded Message: {decoded_message}")
        elif choice == 'q':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
