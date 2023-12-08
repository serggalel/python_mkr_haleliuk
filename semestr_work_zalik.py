word1 = input("Введіть перше слово, яке потрібно буде замінити: ")
word2 = input("Введіть друге слово, яке замінить перше: ")

file = open("zalik_file", "r", encoding='UTF-8')
file_text = file.read()
if word1 in file_text:
    replaced_text = file_text.replace(word1, word2)

    file2 = open("zalik_file", "w", encoding='UTF-8')

    file2.write(replaced_text)
    file2.close()
else:
    print("Такого слова немає у файлі!")







