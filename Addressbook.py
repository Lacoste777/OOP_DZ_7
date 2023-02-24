from Phonebook import *


pb = []
pb.append(Phonebook("Петрова Анастасия Ивановна", "8904444444", "Волгоград"))
pb.append(Phonebook("Сергеев Павел Васильевич", "89053333333", "Обнинск"))
pb.append(Phonebook("Коростин Константин Витальевич", "896087055555", "Москва"))


def show_addressbook():
    for i in pb:
        print(i.get_name(), i.get_phone(), i.get_city())