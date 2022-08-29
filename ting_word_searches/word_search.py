def exists_word(word, instance):
    occurrence = []
    words_report = []
    for index, line in enumerate(instance._data[0]['linhas_do_arquivo']):
        if word.lower() in line.lower():
            occurrence.append({'linha': index + 1})
    if len(occurrence) > 0:
        words_report = [
            {
                "palavra": word,
                "arquivo": instance._data[0]['nome_do_arquivo'],
                "ocorrencias": occurrence,
            }
        ]
    return words_report


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
