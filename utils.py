import json


def load_candidates():
    """
    Загружает данные из json файла
    """
    with open('candidates.json', encoding='utf-8') as f:
        return json.load(f)


def get_all():
    """
    Возвращает данные из функции load_candidates()
    :return: list(список кандидатов)
    """
    return load_candidates()


def get_by_pk(pk):
    """
    Возвращает данные кандидата по порядковому номеру.
    Если заданного pk нет в списке - ничего не возвращается.
    :param pk: int(порядковый номер)
    :return: dict(данные кандидата)
    """
    candidates = load_candidates()
    for candidate in candidates:
        if candidate['pk'] == pk:
            return candidate
    return


def get_by_skill(skill_name):
    """
    Возвращает список кандидатов, обладающих заданным навыком(skill_name)
    :param skill_name: навык кандидата
    :return: list(список кандидатов)
    """
    candidates = []
    for candidate in load_candidates():
        if skill_name.lower() in candidate['skills'].lower().split(', '):
            candidates.append(candidate)
    return candidates
