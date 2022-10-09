



while True:
    try:
        string = input("Ваша строка: ")
        if string.isalpha() and len(string) >2:
            file = open(".\\dir\\" + string + ".txt","w+")
        else:
            print("Введите другую строку, длина которой будет больше 2 и будет содержать только буквы")
    finally:
        file.close()
