"""Головний модуль"""
import sys
from pathlib import Path
from file_manager.process_directory import process_directory

def sort_folder(folder: str) -> None:
    """ Головна функція обробки папки

    Args:
        folder (str): передаем шлях до папки
    """
    folder_path = Path(folder)
    sorted_folder_path = folder_path
    process_directory(folder_path, sorted_folder_path)