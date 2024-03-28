# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 12:14:30 2021

@author: user
"""

def encrypt_cc(original_message, key):
    alphabet = ('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    #key = 3
    #original_message = ('I love programming')
    original_message = original_message.upper()
    encrypted_message = ('')
    
    for char in original_message:
        if char in alphabet:
            char_pos = alphabet.find(char) + key
            if char_pos > (len(alphabet) - 1):
                char_pos = char_pos % len(alphabet) -1
            char = alphabet[char_pos]
        else:
            char == char
        encrypted_message += char
    return encrypted_message
            
original_message = ('I love programming')
key = 3
print(encrypt_cc(original_message, key))

#Decrypting 

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
print(decrypt_cc(encrypted_message, key))
