""" normalize string to latin"""

def normalize(input_str: str) -> str:
    """ function change cyrillic to latin chars"""
    # Створюємо словник для транслітерації кирилічних символів на латиницю
    transliteration_dict = {
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'h',
        'д': 'd', 'е': 'e', 'є': 'ie', 'ж': 'zh', 'з': 'z', 'и': 'y',
        'і': 'i', 'ї': 'yi', 'й': 'i', 'к': 'k',
        'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r',
        'с': 's', 'т': 't', 'у': 'u', 'ф': 'f',
        'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh',
        'щ': 'shch', 'ь': '', 'э': 'e', 'ю': 'iu', 'я': 'ia'
    }
    result_str = ''
    for char in input_str:
        # Перевіряємо, чи є символ у словнику транслітерації
        if char.lower() in transliteration_dict:
            # Замінюємо на відповідне значення зі словника
            if char.isupper():
                result_str += transliteration_dict[char.lower()].capitalize()
            else:
                result_str += transliteration_dict[char.lower()]
        # Якщо символ не є літерою кирилічного або латинського алфавіту, замінюємо на "_"
        elif not char.isalnum():
            result_str += '_'
        else:
            result_str += char
    return result_str


if __name__ == "__main__":
    INPUT_STRING = "Привіт123, світ45!"
    normalized_str = normalize(INPUT_STRING)
    print(normalized_str)
