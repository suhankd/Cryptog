def CBC_Vig():

    def XOR_gate(block1,block2):
        bytes1 = bytes(block1,'utf-8')
        bytes2 = bytes(block2,'utf-8')
        result_bytes = bytearray()
        for byte1,byte2 in zip(bytes1,bytes2):
            result_byte = byte1 ^ byte2
            result_bytes.append(result_byte)
        result_string = result_bytes.decode('utf-8')
        return result_string
    
    def find_size():
        while True:
            try:
                size = int(input("Enter the size of each block. "))
                return size
            except ValueError:
                print("Please enter a valid number.")
    size = find_size()

    def get_IV():
        while True:
            IV = input("Enter the Initialization vector. ")
            if len(IV) != size:
                print("Invalid size. Please select an IV of ",size,"characters. ")
            else:
                return IV   
    IV = get_IV()

    def get_message():
        message = input("Enter a message to encrypt. ")
        return message
    message = get_message()

    def get_key():
        key = input("Enter the key. ")
        if any(char.isdigit() for char in key):
            raise ValueError("Input string contains an integer. ")
        return key  
    key = get_key()

    def extended_string(string,len_block):
        current_len = len(string)
        remainder = current_len%len_block
        if remainder == 0:
            return string
        padding = (len_block - remainder)*" "
        extended_string = string + padding
        return extended_string
    
    # Vigenere Cipher

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
    
    def encryption(s):
            if s == 0:
                XORed_val = XOR_gate(IV,calibrated_message[s*size:((s+1)*size)])
            else:
                XORed_val = XOR_gate(encryption(s-1),calibrated_message[s*size:(((s+1)*size)+1)])
            Vigged_val = vigenere_cipher(XORed_val,key)
            return Vigged_val
    
    calibrated_message = extended_string(message,size)

    encrypted_text = ""

    for i in range(0,int((len(calibrated_message)/size)-1)):
        encrypted_string = encryption(i)
        encrypted_text += encrypted_string
    return encrypted_text

        
print(CBC_Vig())      


