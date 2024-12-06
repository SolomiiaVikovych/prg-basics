def read_from_file(name):
   with open(name) as file:
      content = file.read()
   return content

file_content = read_from_file('pets.txt')
file_lines = file_content.splitlines()

file_lines_list = file_content.split()

number_of_words = len(file_lines_list)

print('number of words: ', number_of_words)