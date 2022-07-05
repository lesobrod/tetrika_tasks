import wikipediaapi


def get_animals_count(all_animals, letter):
    counter = 0
    for animal in all_animals.values():
        if animal.title[:1] == letter:
            counter += 1
    return counter


if __name__ == "__main__":
    wiki = wikipediaapi.Wikipedia('ru')
    letters = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЭЮЯ'
    cat = wiki.page("Категория:Животные_по_алфавиту")
    print("Please wait...")
    all_animals = cat.categorymembers
    for letter in letters:
        animals_count = get_animals_count(all_animals, letter)
        print(f'{letter}: {animals_count}')
