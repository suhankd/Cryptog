def atbash_cipher():
    def encrypt_atbash(message):
        encrypted_text = ""
        for char in message:
            if char.isalpha():
                encrypted_char = chr(219-ord(char)) if char.islower() else chr(155-ord(char))
                encrypted_text += encrypted_char
            elif char.isdigit():
                encrypted_char = chr(105-ord(char))
                encrypted_text += encrypted_char
            else:
                encrypted_text += char
        return encrypted_text
    def UI():
        while True:
            print("The encrypted text is :",encrypt_atbash(input("Enter a text to encrypt.")))
            q_or_c = input("Press 'q' to exit, and any other key to continue.")
            if q_or_c == "q":
                break
    UI()