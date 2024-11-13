def palindrom(sentence):
    is_palindrom = False
    if sentence == sentence[::-1]:
        is_palindrom = True
    return is_palindrom

user_sentence = input(' enter sentence ')
print(f' sentence {user_sentence} is palindrom: {palindrom(user_sentence)}')    