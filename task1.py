documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def people(documents):
    number = input('Введите номер документа ')
    for document in documents:
        if number == document['number']:
            return document['name']
    return 'Документ не найден'


#Функция вывода номера полки по номеру документа
def shelf(directories):
    number = input('Введите номер документа ')
    for key, value in directories.items():
        if number in value:
            return key
    return 'Документ не найден'


#Функция вывода списка всех документов
def list(documents):
    for document in documents:
        print(f'{document["type"]}, "{document["number"]}", {document["name"]}')


#Функция добавления нового документа в каталог и в перечень полок
def add(documents, directories):
    type = input('Введите тип документа ')
    number = input('Введите номер документа ')
    name = input('Введите имя владельца ')
    shelf = input('Введите номер полки ')
    if shelf not in directories:
        return 'Такой полки нет'
    new_document = dict(type=type, number=number, name=name)
    documents.append(new_document)
    directories[shelf].append(number)
    return 'Документ добавлен'


#Функция удаления документ из каталога и его номер из перечня полок
def delete(documents, directories):
    number = input('Введите номер документа ')
    for document in documents:
        if number == document['number']:
            documents.remove(document)
    for key, value in directories.items():
        if number in value:
            value.remove(number)
            return 'Документ удален'
    return 'Документ не найден'


#Функция переноса с одной полки на другую
def move(directories):
    number = input('Введите номер документа ')
    shelf = input('Введите номер полки ')
    if shelf not in directories:
        return 'Полка не найдена'
    for key, value in directories.items():
        if number in value:
            directories[shelf].append(number)
            value.remove(number)
            return 'Документ перемещен'
    return 'Документ не найден'


#Функция добавления новой полки
def add_shelf(directories):
    shelf = input('Введите номер новой полки ')
    if shelf in directories:
        return 'Такая полка уже существует'
    directories[shelf] = []
    return 'Полка добавлена'



def check_user_command():
    print(
        "\np - people – Показать имя человека по номеру документа, "
        "\nl – list – Показать список всех документов, "
        "\ns – shelf – Показать номер полки по номеру документа"
        "\na – add – добавить новый документ"
        "\nd – delete – удалить документ"
        "\nm – move – перенос документа на другую полку"
        "\nas – add_shelf – добавление новой полки"
      )
    user_command = input('\nВведите команду: ')
    if user_command == 'p':
        return(people(documents))
    elif user_command =='l':
        return(list(documents))
    elif user_command == 's':
        return(shelf(directories))
    elif user_command == 'a':
        return(add(documents, directories))
    elif user_command == 'd':
        return(delete(documents, directories))
    elif user_command == 'm':
        return(move(directories))
    elif user_command == 'as':
        return(add_shelf(directories))
    else:
        return('Неизвестная команда')
print(check_user_command())



