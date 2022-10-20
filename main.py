def translate():
    word = input("Podaj słowko po polsku: ")

    if(word in dictionary):
        print(dictionary[word])
    else:
        print("Brak słówka")

def add():
    wordPL = input("Podaj słowko po polsku: ")
    wordENG = input("Podaj słowko po angielsku: ")
    dictionary[wordPL] = wordENG
    print(dictionary)

def dele():
    wordPL = input("Podaj po polsku co usunąć: ")
    dictionary.pop(wordPL)
    print(dictionary)
while(True):
    choice = input("1. Tłumacz, 2. Dodaj, 3. Usuń, 4. Exit")
    if(choice == "1"):
        translate()
    elif(choice == "2"):
        add()
    elif(choice =="3"):
        dele()
    elif(choice =="4"):
        exit()

