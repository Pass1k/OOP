def check_permission(*permissions):
    def decorator(func):
        def wrapper(*args, **kwargs):
            user_permissions = ['admin']  # здесь нужно получать разрешения пользователя из базы данных или сессии
            for permission in permissions:
                if permission in user_permissions:
                    return func(*args, **kwargs)
            raise PermissionError(f'У пользователя недостаточно прав, чтобы выполнить функцию {func.__name__}')
        return wrapper
    return decorator


user_permissions = ['admin']


@check_permission('admin')
def delete_site():
    print('Удаляем сайт')


@check_permission('user_1')
def add_comment():
    print('Добавляем комментарий')


delete_site()
add_comment()