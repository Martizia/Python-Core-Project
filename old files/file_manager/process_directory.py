"""Обробка каталогу та його підкаталогів."""
from pathlib import Path
from file_manager.process_file import process_file

def process_directory(directory_path: Path, sorted_folder_path: Path) -> None:
    """Рекурсивна обробка каталогу та його підкаталогів."""
    # Створюємо список для зберігання папок та файлів для подальшого сортування
    folders_to_sort = []
    for item in directory_path.iterdir():
        # якщо файл, обробляємо окремою функціею
        if item.is_file():
            process_file(item, sorted_folder_path)
        elif item.is_dir():
            # Додаємо папку до списку, щоб обробити її пізніше
            folders_to_sort.append(item)
    # Обробляємо папки за зворотнім порядком, оскільки ми вище зберегли їх у порядку вкладеності
    for folder in reversed(folders_to_sort):
        process_directory(folder, sorted_folder_path)
    # Видаляємо порожні папки
    for item in directory_path.iterdir():
        if item.is_dir() and not list(item.iterdir()):
            item.rmdir()
