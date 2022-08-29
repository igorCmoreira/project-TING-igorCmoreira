import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for index in range(len(instance)):
        if instance.search(index)["nome_do_arquivo"] == path_file:
            return None
    data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(txt_importer(path_file)),
        "linhas_do_arquivo": txt_importer(path_file)
    }
    instance.enqueue(data)
    print(data)


def remove(instance):
    if instance.is_empty():
        return print("Não há elementos", file=sys.stdout)
    att_list = instance.dequeue()
    return print(f"Arquivo {att_list['nome_do_arquivo']} removido com sucesso")


def file_metadata(instance, position):
    if position > 0 or position > instance.__len__() - 1:
        return print("Posição inválida", file=sys.stderr)
    arq = instance.search(position)
    path_file = arq['nome_do_arquivo']
    data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(txt_importer(path_file)),
        "linhas_do_arquivo": txt_importer(path_file)
    }
    print(f"Arquivo {data} removido com sucesso")
