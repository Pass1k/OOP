user_name = input('Введите имя:')

while True:
    print('Чтобы увидеть текущий текст чата введите 1, чтобы написать сообщение ведите 2')
    response = input('Ввидите 1 или 2\n')
    if response == '1':
        try:
            with open('chat.txt', 'r') as file:
                messages = file.readline()
                print(''.join(messages))
        except FileNotFoundError:
            print('Служебное сообщение: пока ничего нет\n')
    elif response == '2':
        new_message = input('Введите сообщение: ')
        with open('chat.txt', 'a') as file:
            file.write('{name}: {message}\n'.format(
                name=user_name, message=new_message
            ))
    else:
        print('Неизвестная команда\n')