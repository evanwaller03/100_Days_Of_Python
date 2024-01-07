def encode(message, shift_number):
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

        elif encode_or_decode == 'd':
            input_not_validated = False
            message_to_decode = input("Message to decode: ")
            decode_shift_number = int(input("Shift number: "))
            decoded_message = decode(message_to_decode, decode_shift_number)
    #       