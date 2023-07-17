from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    # Verifica se o arquivo já foi processado anteriormente
    for index in range(len(instance)):
        if instance.search(index)["nome_do_arquivo"] == path_file:
            return

    # Importa as linhas do arquivo
    file_lines = txt_importer(path_file)

    # Cria o dicionário com os dados do arquivo
    file_data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file_lines),
        "linhas_do_arquivo": file_lines,
    }

    # Adiciona o dicionário à fila
    instance.enqueue(file_data)

    # Exibe os dados processados via stdout
    sys.stdout.write(str(file_data))


def remove(instance):
    if len(instance) == 0:
        print("Não há elementos")
        return

    removed_file = instance.dequeue()
    print(f"Arquivo {removed_file['nome_do_arquivo']} removido com sucesso")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
