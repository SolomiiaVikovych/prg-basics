def remove_space(text):
    new_text = text.replace(" ", "")
    return new_text

sentence = input('enter sentence ')
print(f' your sentence without space is {remove_space(sentence)}')
