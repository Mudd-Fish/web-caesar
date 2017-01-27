def encrypt(text, rot):
    return rotate_char(text, rot)

def rotate_char(mess, rot):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    up_alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    encrypted = ''

    for char in mess:
        if(char.isalpha()) == False:
            encrypted = encrypted + char

        elif(char == str.lower(char)):
            rotated_index = alphabet_position(char) + rot
            if rotated_index < 26:
                encrypted = encrypted + alphabet[rotated_index]
            else:
                encrypted = encrypted + alphabet[rotated_index % 26]

        elif(char == str.upper(char)):
            rotated_index = alphabet_position(char) + rot
            if rotated_index < 26:
                encrypted = encrypted + up_alpha[rotated_index]
            else:
                encrypted = encrypted + up_alpha[rotated_index % 26]
    return encrypted

def alphabet_position(input):

    lower = str.lower(input)
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    for x in alphabet:
        if(x == lower):
            return alphabet.index(x)
    else:
        return False

