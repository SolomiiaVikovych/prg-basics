translations = {
   'computer': 'komputer',
   'mouse': 'myszka',
   'keyboard': 'klawiatura',
   'printer': 'drukarka'
}
word = input('enter word to translate: ')
for key in translations():
    if word == key:
        print(f'{word} in polish is {translations[word]}')
    else:
        print("No such word in a dictionary")