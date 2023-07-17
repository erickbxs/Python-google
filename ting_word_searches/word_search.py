def exists_word(word, instance):
    result = []

    for index in range(len(instance)):
        file_data = instance.search(index)
        file_name = file_data["nome_do_arquivo"]
        file_lines = file_data["linhas_do_arquivo"]

        occurrences = []
        for line_num, line in enumerate(file_lines, start=1):
            if word.lower() in line.lower():
                occurrences.append({"linha": line_num})

        if occurrences:
            file_info = {
                "palavra": word,
                "arquivo": file_name,
                "ocorrencias": occurrences,
            }
            result.append(file_info)

    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
