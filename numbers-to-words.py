num_letters = {
  'o': '0',
  'i': '1',
  'e': '3',
  'a': '4',
  's': '5',
  't': '7',
  'b': '8',
}

input_file = 'words.txt'
output_file = 'result.txt'

def is_number_word(word):
  for letter in word:
    if letter not in num_letters.keys():
      return False
  return True

if __name__ == '__main__':
  is_number_word("boobs")

  result = []
  # assumes file is formatted correctly (one word per line, no additional whitespace, all lowercase)
  with open(input_file, 'r') as file:
    for line in file:
      if is_number_word(line[:-1]):
        result.append(line)

  # write result to file
  with open(output_file, 'w') as file:
    for word in result:
      file.write(word)