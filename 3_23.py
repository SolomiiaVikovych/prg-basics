import MyText
var = 'An apple a day keeps the doctor away'
print('Number of words: ', MyText.count_words(var))
print('Words from the longest: ', ' '.join(map(str,MyText.sort_words_by_length(var))) )
print('Words worted alphabeticaly: ', ' '.join(map(str,MyText.sort_words_alphabetically(var))))