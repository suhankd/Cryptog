def Substring_Reposition_Cipher():
    def get_var_graph():
        user_input = input("Enter the number of letters you want in a group: ")
        try:
            var_graph = int(user_input)
            return var_graph
        except ValueError:
            print("Invalid input. Please enter an integer.")
            return get_var_graph()
        
    def get_msg():
        user_input = input("Enter the message you would like to encrypt. ")
        return user_input
    
    def subSRC(message,var_graph):
        encrypted_message = ""
        no_of_strings = int(len(message)//var_graph)
        for i in range(0,no_of_strings):
            sub_string = message[i*var_graph:(i+1)*var_graph]
            encrypted_sub_string = ""
            for s in range(0,len(sub_string)):
                encrypted_sub_string += sub_string[(s+1)%len(sub_string)]
            encrypted_message += encrypted_sub_string
        return encrypted_message     
    print(subSRC(get_msg(),get_var_graph()))  
Substring_Reposition_Cipher()

            





    