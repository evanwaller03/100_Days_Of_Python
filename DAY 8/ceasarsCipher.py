normal_alphabet = 'abcedfghijklmnopqrstuvwxyz'
chars_to_skip = ['.', ' ', ',', "'", '!', '$']

def encode(message, shift_number):
    encoded_message = ''
    for letter in message.lower():
        if letter in chars_to_skip:
            encoded_message = encoded_message + letter
            continue
            
        current_index  = normal_alphabet.index(str(letter))
        if (current_index + shift_number) >= len(normal_alphabet):
            new_index = (current_index + shift_number) - len(normal_alphabet)
        else: 
            new_index = current_index + shift_number
        encoded_message = encoded_message + normal_alphabet[new_index]
    
    return encoded_message

def decode(message, shift_number):
    decoded_message = ''
    for letter in message.lower():
        if letter in chars_to_skip:
            decoded_message = decoded_message + letter
            continue
            
        current_index  = normal_alphabet.index(str(letter))
        if (current_index - shift_number) < 0:
            new_index = (current_index - shift_number) + len(normal_alphabet)
        else: 
            new_index = current_index - shift_number
        decoded_message = decoded_message + normal_alphabet[new_index]
    
    return decoded_message

print("Welcome to Ceasars Cipher.")

run_again = True

while run_again:
    # Take Input
    encode_or_decode = input("Would you like to encode(e) or decode(d)?\nSelection: ")
    if encode_or_decode == 'e':
        message_to_encode = input("Message to encode: ")
        set_shift_number = int(input("Shift number: "))
        encoded_message = encode(message_to_encode, set_shift_number)
        print(encoded_message)

    elif encode_or_decode == 'd':
        message_to_decode = input("Message to decode: ")
        decode_shift_number = int(input("Shift number: "))
        decoded_message = decode(message_to_decode, decode_shift_number)
        print(decoded_message)
    
    play_again = input("Again? (Y) or (N)").lower()
    if play_again == "n":
        run_again = False