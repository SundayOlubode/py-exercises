def decrypt_cc(encrypted, key):
    decrypted_message = ('')
    alphabet = ('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    for char in encrypted:
        if char in alphabet:
            char_pos = (alphabet.find(char) - key)
            if char_pos < 0:
                char_pos += len(alphabet)
            new_char = alphabet[char_pos]
        else:
            new_char = char
        decrypted_message += new_char
    return (decrypted_message)
encrypted_message = ('L ORYH SURJUDPPLQJ')
key = 3
print(decrypt_cc(encrypted_message, key,), '\n')


def hack_cc(encrypted_message):
    for key in range(26):
        print(decrypt_cc(encrypted_message, key))

hack_cc(encrypted_message)