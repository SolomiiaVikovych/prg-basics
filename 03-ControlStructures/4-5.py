#
plain_text = 'The early bird catches the worm'
encrypted_text = ''

for char in plain_text:
    char_encoded = ord(char)
    char_encoded = char_encoded+ 1
    encrypted_text =  encrypted_text + chr(char_encoded) 
  


    # read the character's code (use ord())
    ...
    # add one to the character's code
    ...
    # replace new character code with its
    # corresponding character (use chr())
    ...
    # add encrypted character to encrypted text
    ...

print(plain_text)
print(encrypted_text)