
from pathlib import Path
import shutil
from file_manager.normalize import normalize


def process_file(file_path: Path, target_folder: Path) -> None:
    """Process a file by moving it to the target folder and renaming it."""
    file_extension = file_path.suffix[1:].lower()
    categories = {
        'images': ['jpeg', 'png', 'jpg', 'svg', 'gif', 'svg'],
        'videos': ['avi', 'mp4', 'mov', 'mkv'],
        'documents': ['doc', 'docx', 'txt', 'pdf', 'xlsx', 'pptx', 'html'],
        'music': ['mp3', 'ogg', 'wav', 'amr'],
        'archives': ['zip', 'gz', 'tar'],
    }
    category = None
    for cat, extensions in categories.items():
        if file_extension in extensions:
            category = cat
            break
    if category is None:
        category = 'unknown'

    
    try:
        # Working with archives, extracting their content
        if category == 'archives':
            archive_folder_name = normalize(file_path.stem)
            archive_folder = target_folder / 'archives' / archive_folder_name
            # unpack archive file in archive folder
            shutil.unpack_archive(str(file_path), str(archive_folder))
            # move archive file to unpack folder
            shutil.move(str(file_path), str(archive_folder / file_path.name))
    except shutil.ReadError as e:
        print(f"Error processing archive at '{file_path}': {e}")
    except Exception as e:
        print(f"An unexpected error occurred while processing '{file_path}': {e}")
    else:
        new_file_name = normalize(file_path.stem) + file_path.suffix
        target_path = target_folder / category / new_file_name
        target_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(file_path), str(target_path))
        