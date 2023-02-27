phonebook_all='phonebook.txt'

def read_phonebook(): 
    print(f'В справочнике содержаться следующие контакты:\n')
    with open(phonebook_all, 'r', encoding='utf8') as book: 
        for line in book:
            print(line.replace("\r", "").replace("\n","")) 
 
def search_record(name):
    print('Найден следуюший контакт:')
    with open(phonebook_all, 'r', encoding='utf8') as book: 
        for line in book:
           if name in line:
               print(line.replace("\r", "").replace("\n","")) 
               
def add_lines_phonebook(new_contact): 
    with open(phonebook_all, 'a', encoding='utf8') as book: 
        book.write(new_contact +'\n') 
        print('Новая запись была успешно добавлена в телефонный справочник!')

def line_replacement(name,new_name): 
    with open(phonebook_all, 'r',  encoding='utf8') as book:
       x=book.read()
    with open(phonebook_all, 'w',  encoding='utf8') as book:
        x=x.replace(name,new_name)
        book.write(x)
        print('Данные были успешно изменены!')
    
def remove_contact(name):
    with open(phonebook_all, 'r', encoding="utf-8") as book:
        x = book.readlines()
    with open(phonebook_all, 'w', encoding="utf-8") as book:
        count=0
        for line in x:
            if  name in line:
                count=+1
            else:
                book.write(line)
        if count == 0:
            print('Нет данных, удовлетворяющих введенным значениям!')
        else:
             print("Запись в телефонном справочнике удалена!")

def request_from_the_user(): 
    while True:
        number=int(input(f'Введите:\n'
                '1 - для просмотра данных телефонного справочника;\n'
                '2 - для поиска контакта;\n'
                '3 - для добавления контакта;\n'
                '4 - для изменения данных;\n'
                '5 - для удаления контакта;\n'
                '6 - для выхода из программы:\n')) 
        while (number<1) or (number>6) :
            number= int(input('Введите значение от 1 до 6: '))
        if number == 1: 
            read_phonebook()
        elif number == 2: 
            search_record(input('Введите данные для поиска: ')) 
        elif number == 3: 
            add_lines_phonebook(input('Внесите ФИО и телефон для записи в телефонный справочник: ')) 
        elif number == 4:
            line_replacement(input('Введите данные, которые хотите изменить: '),input('на '))
        elif number==5:
            remove_contact(input('Введите данные, которые хотите удалить: '))
        elif number == 6:
            exit()

request_from_the_user()