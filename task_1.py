def simple_text_editor():
    filename = input("Введіть назву файлу (з .txt): ")

    print("Введіть текст (порожній рядок — завершення вводу):")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    with open(filename, "w", encoding="utf-8") as file:
        for line in lines:
            file.write(line + "\n")

    print("\nВміст створеного файлу:")
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read())

simple_text_editor()
