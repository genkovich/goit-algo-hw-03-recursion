from pathlib import Path
import shutil
import argparse


def parse_input():
    parser = argparse.ArgumentParser(description="Copy files from source to dist")
    parser.add_argument("--source", help="Source directory", required=True, type=Path)
    parser.add_argument("--dist", help="Destination directory", default=Path("dist"), type=Path)

    return parser.parse_args()


def copy_files(directory, dist):
    try:
        path = Path(directory)
        for element in path.iterdir():
            if element.is_dir():
                copy_files(element, dist)
            if element.is_file():
                print(f"Parse folder: This is file - {element.name}")
                file_type = parse_filetype(element)
                type_dir = Path(dist) / file_type
                type_dir.mkdir(exist_ok=True, parents=True)
                shutil.copy(element, type_dir)
    except Exception as e:
        print(f"Copy error: {e}")


def parse_filetype(file):
    extension = file.suffix

    file_types = {
        'text': ['.txt', '.doc', '.docx', '.rtf', '.pdf', '.xlsx', '.csv', '.xls'],
        'code': ['.py', '.html', '.css', '.js', '.java', '.php', '.c', '.cpp', '.h', '.hpp', '.cs', '.go'],
        'config': ['.xml', '.json', '.yaml', '.yml', '.ini'],
        'video': ['.avi', '.mp4', '.mov', '.mkv'],
        'image': ['.jpeg', '.png', '.jpg', '.gif'],
        'audio': ['.mp3', '.ogg', '.wav', '.amr'],
        'archive': ['.zip', '.gz', '.tar', '.rar'],
    }

    for file_type, extensions in file_types.items():
        if extension in extensions:
            return file_type

    return 'other'



