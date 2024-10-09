import os
import json
from package.functions import process_numbers, translate_text

DATA_FILE = 'MyData.json'

# Функція для читання даних з файлу
def read_data_from_file():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r') as file:
                data = json.load(file)
                return data
        except (json.JSONDecodeError, KeyError):
            print("Некоректні дані у файлі.")
            return None
    return None

# Функція для запису даних у файл
def write_data_to_file(numbers, language):
    data = {"numbers": numbers, "language": language}
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file)
    print(f"Дані збережено в файл {DATA_FILE}")

# Функція для введення даних від користувача
def get_user_input():
    numbers = list(map(int, input("Введіть три числа a, b, c: ").split()))
    language = input("Введіть мову інтерфейсу (uk/en): ").lower()
    write_data_to_file(numbers, language)
    print("Робота завершена.")

def main():
    data = read_data_from_file()
    
    if data is None:  # Якщо немає даних або вони некоректні
        get_user_input()
    else:
        # Отримуємо дані
        language = data.get('language', 'uk')
        numbers = data.get('numbers')
        
        # Перевірка на коректність мови
        if language not in ['uk', 'en']:
            language = 'uk'
        
        # Виводимо мову
        print(translate_text("Мова:", language), language.capitalize())
        
        # Працюємо з числами
        print(translate_text("Три числа a, b, c:", language), f"{numbers[0]} {numbers[1]} {numbers[2]}")
        
        # Обробляємо числа
        result = process_numbers(numbers)
        print(translate_text("Додатні возвести в куб, а від’ємні замінити на 0:", language), f"{result[0]} {result[1]} {result[2]}")
        
        # Порівнюємо числа
        positives = [n for n in result if n > 0]
        comparison = " < ".join(map(str, sorted(positives)))
        print(comparison)

if __name__ == "__main__":
    main()