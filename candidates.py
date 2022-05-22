import json

class Candidates:
    def __init__(self, url):
        self.url = url

    def load_date(self):
        '''
        Метод принимает файл JSON формата, читает, преобразует прочитанное в формат Python.
        :return: list.
        '''
        with open(self.url, 'r', encoding='utf-8') as file:
            candidates = json.load(file)   #list(json.loads(file.read()))
        return candidates

    def choiсe_id(self, id):
        '''
        Метод выбирает из списка, полученного с помощью метода load_date, нужный элемент по номеру в
        базе и возвращает информацию о выбранном кандидате.
        :param id: int (порядковый номер кандидата в базе).
        :return: dict (информация о выбранном кандидате).
        '''
        candidates = self.load_date()

        for candidate in candidates:
            if id == candidate['id']:
                return candidate

    def search_result(self, name_search):
        '''
        Метод выбирает из списка, полученного с помощью метода load_date, элементы, в имени которых
        содержится заданное строковое значение и возвращает результат поиска.
        :param name: str (имя кандидата в базе)
        :return: list (список с информацией о выбранных кандидатах)
        '''
        search_result = []
        candidates = self.load_date()

        for candidate in candidates:
            if name_search.lower() in candidate['name'].lower():
                search_result.append(candidate)

        return search_result

    def choiсe_skills(self, skill):
        '''
        Метод выбирает из списка, полученного с помощью метода load_date, информацию о кандидатах, имеющих
        заданный навык и возвращает результат поиска.
        :param skill: str (искомый навык)
        :return: list (список с информацией о выбранных кандидатах)
        '''
        candidates_with_skills = []
        candidates = self.load_date()

        for candidate in candidates:
            skills = candidate['skills'].lower().split(', ')
            if skill.lower() in skills:
                candidates_with_skills.append(candidate)
        return candidates_with_skills
