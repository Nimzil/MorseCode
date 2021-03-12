MORSE_DICT = {'A': '.-', 'B': '-...',
              'C': '-.-.', 'D': '-..', 'E': '.',
              'F': '..-.', 'G': '--.', 'H': '....',
              'I': '..', 'J': '.---', 'K': '-.-',
              'L': '.-..', 'M': '--', 'N': '-.',
              'O': '---', 'P': '.--.', 'Q': '--.-',
              'R': '.-.', 'S': '...', 'T': '-',
              'U': '..-', 'V': '...-', 'W': '.--',
              'X': '-..-', 'Y': '-.--', 'Z': '--..',
              '1': '.----', '2': '..---', '3': '...--',
              '4': '....-', '5': '.....', '6': '-....',
              '7': '--...', '8': '---..', '9': '----.',
              '0': '-----', ', ': '--..--', '.': '.-.-.-',
              '?': '..--..', '/': '-..-.', '-': '-....-',
              '(': '-.--.', ')': '-.--.-'}


def encrypt_text():
    user_input = input('Enter a message to decrypt:  ').upper()
    morse = ''
    for letter in user_input:
        if user_input != ' ':
            morse += f"{MORSE_DICT[letter]} "
        else:
            morse = ''
    return morse


def decrypt_text():
    user_input = input('Enter your morse code message to decrypt: ').split(' ')
    code_reversed = {value: key for key, value in MORSE_DICT.items()}
    message = ''
    for code in user_input:
        if user_input != " ":
            message += f"{code_reversed[code]}"

    return message.capitalize()


counter = 5
while counter > 0:
    user_choice = input("Please enter 'Encrypt' or 'Decrypt' or 'q' to quite.: ").lower()

    if user_choice == 'encrypt':
        print(encrypt_text())
        break
    elif user_choice == 'decrypt':
        print(decrypt_text())
        break
    elif user_choice == 'q':
        break
    else:
        counter -= 1
