import time

def translate():
    # word = input("Podaj słowko po polsku: ")
    fileo = open("dictionary.txt", "r", encoding="UTF-8")
    dictionary = {}
    for wiersz in fileo:
        wierszTab = wiersz.split(":")
        print(wierszTab[0], end="")
        print(wierszTab[1], end="")
        dictionary[wierszTab[0]] = wierszTab[1].replace("\n", "")
    print(dictionary)

    # if(word in dictionary):
    #     print(dictionary[word])
    # else:
    #     print("Brak słówka")


translate()
# def add():
#     wordPL = input("Podaj słowko po polsku: ")
#     wordENG = input("Podaj słowko po angielsku: ")
#     dictionary[wordPL] = wordENG
#     print(dictionary)
#
# def dele():
#     wordPL = input("Podaj po polsku co usunąć: ")
#     dictionary.pop(wordPL)
#     print(dictionary)
#
# while(True):
#     choice = input("1. Tłumacz, 2. Dodaj, 3. Usuń, 4. Exit")
#     if(choice == "1"):
#         translate()
#     elif(choice == "2"):
#         add()
#     elif(choice =="3"):
#         dele()
#     elif(choice =="4"):
#         exit()
#
