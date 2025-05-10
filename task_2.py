def analyze_file():
    filename = input("Введіть назву файлу для аналізу: ")

    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()

    lines = text.splitlines()
    words = text.split()
    characters = len(text)

    print("\nАналіз файлу:")
    print(f"Рядків:     {len(lines)}")
    print(f"Слів:       {len(words)}")
    print(f"Символів:   {characters}")

analyze_file()
