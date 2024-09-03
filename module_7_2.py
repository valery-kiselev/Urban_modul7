def custom_write(file_name, strings):
    dictionary = {}
    file = open(file_name, 'w', encoding='utf-8')
    j = 1
    for i in strings:
        dictionary[(j, file.tell())] = i
        file.write(f'\n{i}')
        j += 1
    return dictionary
    file.close()

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
