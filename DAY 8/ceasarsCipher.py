normal_alphabet = 'abcedfghijklmnopqrstuvwxyz'

def encode(message, shift_number):
    for n in range(0, len(normal_alphabet)):
        if (n + shift_number) > len(normal_alphabet):
            new_index = (n + shift_number) - len(normal_alphabet)
        else: 
            new_index = n + shift_number
        
    return 

def decode(message, shift_number):

    return

print("Welcome to Ceasars Cipher.")

run_again = True

while run_again:
    # Take Input
    input_not_validated = True
    while input_not_validated:
        encode_or_decode = input("Would you like to encode(e) or decode(d)?\nSelection: ")
        if encode_or_decode == 'e':
            input_not_validated = False
            message_to_encode = input("Message to encode: ")
            set_shift_number = int(input("Shift number: "))
            encoded_message = encode(message_to_encode, set_shift_number)
            print(encoded_message)

        elif encode_or_decode == 'd':
            input_not_validated = False
            message_to_decode = input("Message to decode: ")
            decode_shift_number = int(input("Shift number: "))
            decoded_message = decode(message_to_decode, decode_shift_number)
    #       