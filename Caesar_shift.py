def caesar_shift_classic():
    def encrypt(message):
        encrypted_text = ""
        for char in message:
            if char.isalpha():
                encrypted_char = chr((ord(char)-94)%26 + 97) if char.islower() else chr(ord(char)-64%26+65)
                encrypted_text += encrypted_char
            else:
                encrypted_char = char
                encrypted_text += encrypted_char
        return encrypted_text
    def decrypt(message):
        encrypted_text = ""
        for char in message:
            if char.isalpha():
                encrypted_char = chr(((ord(char)-100))%26+97) if char.islower() else chr(((ord(char)-66))%26+65)
                encrypted_text += encrypted_char
            else:
                encrypted_char = char
                encrypted_text += encrypted_char
        return encrypted_text
    def UI():
        def get_dore():
            while True:
                d_or_e = input("Would you like to encrypt or decrypt a text?")
                if d_or_e.lower() in ["decrypt","encrypt"]:
                    return d_or_e.lower()
                else:
                    print("Please enter a valid input.")
        while True:
            eord = get_dore()
            if eord == "encrypt":
                print("The encrypted text is :",encrypt(input("Enter the text you would like to encrypt.")))
            elif eord == "decrypt":
                print("The decrypted text is :",decrypt(input("Enter the text you would like to decrypt.")))
            q_or_c = input("Press 'q' to break the loop and any other key to continue.")
            if q_or_c == "q":
                break
    UI()

def caesar_shift_variable():
    def get_shift_val():
        while True:
            user_input = input("Enter the number you'd like the letters to shift by.")
            try:
                shift_val = int(user_input)
                return shift_val
            except ValueError:
                print("Invalid input. Try again.")
    shift_val = get_shift_val()
    def decrypt(message):
        decrypted_text = ""
        for char in message:
            if char.isalpha():
                decrypted_char = chr((ord(char)-97+shift_val)%26+97) if char.islower() else chr((ord(char)-65+shift_val)%26+65)
                decrypted_text += decrypted_char
            else:
                decrypted_text += char 
        return decrypted_text
    def encrypt(message):
        encrypted_text = ""
        for char in message:
            if char.isalpha():
                decrypted_char = chr((ord(char)-97-shift_val)%26+97) if char.islower() else chr((ord(char)-65-shift_val)%26+65)
                encrypted_text += decrypted_char
            else:
                encrypted_text += char
        return encrypted_text
    def UI():
        def get_dore():
            while True:
                d_or_e = input("Would you like to encrypt or decrypt a text?")
                if d_or_e.lower() in ["decrypt","encrypt"]:
                    return d_or_e.lower()
                else:
                    print("Please enter a valid input.")
        while True:
            eord = get_dore()
            if eord == "encrypt":
                print("The encrypted text is :",encrypt(input("Enter the text you would like to encrypt.")))
            elif eord == "decrypt":
                print("The decrypted text is :",decrypt(input("Enter the text you would like to decrypt.")))
            q_or_c = input("Press 'q' to break the loop and any other key to continue.")
            if q_or_c == "q":
                break
    UI()

