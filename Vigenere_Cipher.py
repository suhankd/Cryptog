def vigenere_cipher(message,key):
    key = key.upper()
    encrypted_text = ""
    key_denom = 0
    for msg_char in message:
        if msg_char.isalpha():
            key_char = key[key_denom%len(key)]
            shift = ord(key_char)-ord("A")

            if msg_char.isupper():
                encrypted_msg_char = chr((ord(msg_char)-ord('A')+shift)%26+ord("A"))
            else:
                encrypted_msg_char = chr((ord(msg_char)-ord('a')+shift)%26+ord("a"))
            key_denom += 1
        else:
            encrypted_msg_char = msg_char
        encrypted_text += encrypted_msg_char
    return encrypted_text