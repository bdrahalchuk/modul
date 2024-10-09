# Функція для обробки чисел
def process_numbers(numbers):
    processed = [(n**3 if n > 0 else 0) for n in numbers]
    return processed

# Функція для перекладу тексту
def translate_text(text, language):
    translations = {
        "uk": {
            "Мова:": "Мова:",
            "Три числа a, b, c:": "Три числа a, b, c:",
            "Додатні возвести в куб, а від’ємні замінити на 0:": "Додатні возвести в куб, а від’ємні замінити на 0:",
        },
        "en": {
            "Мова:": "Language:",
            "Три числа a, b, c:": "Three numbers a, b, c:",
            "Додатні возвести в куб, а від’ємні замінити на 0:": "Raise positive numbers to the cube, replace negative with 0:",
        }
    }

    if language in translations and text in translations[language]:
        return translations[language][text]
    else:
        return text
