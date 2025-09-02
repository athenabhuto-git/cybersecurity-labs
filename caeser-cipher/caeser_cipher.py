def caesar_cipher_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():  # Only shift letters
            base = ord('A') if char.isupper() else ord('a')
            # (ord(char) - base) → position in alphabet (0–25)
            # + shift → move forward
            # % 26 → wrap around after Z
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            # Keep spaces, numbers, symbols as they are
            result += char
    return result


def caesar_cipher_decrypt(text, shift):
    # Just call encrypt with negative shift
    return caesar_cipher_encrypt(text, -shift)


if __name__ == "__main__":
    print("🔐 Caesar Cipher Tool")
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").upper()
    message = input("Enter your message: ")
    shift = int(input("Enter shift value (e.g., 3): "))

    if choice == "E":
        print("Encrypted Text:", caesar_cipher_encrypt(message, shift))
    elif choice == "D":
        print("Decrypted Text:", caesar_cipher_decrypt(message, shift))
    else:
        print("Invalid choice!")
