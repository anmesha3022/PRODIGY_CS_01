def caesar_cipher():
    print("--- Caesar Cipher Program ---")
    
    # 1. User Choice: Encrypt or Decrypt
    mode = input("Select mode (E for Encryption, D for Decryption): ").upper()
    if mode not in ['E', 'D']:
        print("Invalid mode selected.")
        return

    # 2. Input Message
    text = input("Enter the message: ")
    
    # 3. Input Shift Value (Key)
    try:
        shift = int(input("Enter the shift value (0-25): "))
    except ValueError:
        print("Invalid shift value. Please enter an integer.")
        return

    # Adjust shift for decryption
    if mode == 'D':
        shift = -shift

    result = ""
    for char in text:
        # Check if character is a letter
        if char.isalpha():
            # Determine ASCII base (uppercase or lowercase)
            start = ord('A') if char.isupper() else ord('a')
            # Perform shift and wrap around using modulo 26
            new_char = chr((ord(char) - start + shift) % 26 + start)
            result += new_char
        else:
            # Leave non-alphabetical characters as they are
            result += char

    print(f"Result: {result}")

# Run the program
if __name__ == "__main__":
    caesar_cipher()
