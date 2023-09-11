def XOR_cipher(message,key):
    encrypted_text = ""
    key_denom = 0
    for msg_char in message:
        #Convert the character to its binary representation
        
        bin_msg_char = bin(ord(msg_char))[2:]
        bin_key_char = bin(ord(key[(key_denom)%len(key)]))[2:]

        #ensure that all strings are of the same length

        max_length = max(len(bin_key_char),len(bin_msg_char))
        bin_msg_char = bin_msg_char.zfill(max_length)
        bin_key_char = bin_key_char.zfill(max_length)

        #XOR encryption

        int_XOR_result = int(bin_key_char,2)^int(bin_msg_char,2)

        binXOR_res = chr(int_XOR_result)
        key_denom += 1
        encrypted_text += binXOR_res
    return encrypted_text


msg = input("Enter the message to be encrypted.")
key = input("Enter the key.")
print(XOR_cipher(msg,key))
