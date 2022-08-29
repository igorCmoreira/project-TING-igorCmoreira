import sys


def txt_importer(path_file):
    try:
        if not path_file.endswith(".txt"):
            return print("Formato inválido", file=sys.stderr)
        with open(path_file, encoding="utf-8") as file:
            return [line.strip() for line in file.readlines()]

    except FileNotFoundError:
        return print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
