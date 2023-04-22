text = input("Введите строку: ")

print(list(filter(lambda x: not (x.isupper() or x.isdigit()), text)))