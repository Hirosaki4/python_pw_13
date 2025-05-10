def search_and_replace():
    original_file = input("Введіть назву файлу для обробки: ")
    word_to_find = input("Введіть слово або фразу для пошуку: ")
    replacement = input("Введіть слово або фразу для заміни: ")
    new_file = input("Введіть назву нового файлу (з .txt): ")

    with open(original_file, "r", encoding="utf-8") as file:
        content = file.read()

    new_content = content.replace(word_to_find, replacement)

    with open(new_file, "w", encoding="utf-8") as file:
        file.write(new_content)

    print("Заміна виконана. Результат збережено у новому файлі.")

search_and_replace()
