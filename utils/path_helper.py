import os


def path_helper(file: str):
    if file.startswith('./'):
        file = file[2:]

    return f'{os.path.dirname(os.path.dirname(__file__))}/{file}'
