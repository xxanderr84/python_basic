def user_info(name: str, last_name: str, year_birth: int, city: str, email: str, phone: str):
    """
    Функция для объединения всех данных пользователя
    name: Имя
    last_name: Фамилие
    year_birth: Год рождения
    city: Город
    email: e-mail адрес
    phone: телефон
    :return: строка разделенная пробелами
    """
    tmp_list = [name, last_name, str(year_birth), city, email, phone]
    tmp_str = ' '
    return tmp_str.join(tmp_list)


user_name = input('Введите имя: ')
user_last_name = input('Введите фамилию: ')

while True:
    user_year = input('Введите год рождения: ')
    try:
        user_year = int(user_year)
        break
    except ValueError:
        print('Неверно введен год рождения')

user_city = input('Введите город: ')
user_email = input('Введите email: ')
user_phone = input('Введите номкр телефона: ')
print(user_info(phone=user_phone, email=user_email, city=user_city,
                year_birth=user_year, last_name=user_last_name, name=user_name))
