from my_module import FileLogger

user_log = FileLogger("user_records.log")
print_log = FileLogger("print_messages.log")


class User:
    def __init__(self, init_name, init_age):      
        self._name = init_name
        self._age = init_age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not new_name:
            self.name = 'Безымянный'
            print_log.warn("Пустое имя. Замена имени на 'Безымянный")
            user_log.warn("Пустое имя. Замена имени на 'Безымянный'")
        else:
            self._name = new_name
            user_log.info(f"Задано новое имя пользователя: {new_name}")

    @property
    def age(self):
        return self._age


    @age.setter
    def age(self, new_age):
        if not isinstance(new_age, (int)) or new_age < 0:
            print_log.warn("Некорректный тип данных для возраста")
            user_log.warn("Некорректно задан возраст. Замена возраста на 0")
            self._age = 0
        elif new_age > 120:
            print_log.warn("Завышенный возраст")
            user_log.warn("Установлен возраст больше 120 лет. Замена возраста на 120")
            self._age = 120
        else:
            self.age = new_age
            user_log.info(f"Задан новый возраст: {new_age}")


def check_test():   
    print_log.info('Тестовый прогон.')
    user1 = User("Алиса", 40)
    user2 = User("Боб", 35)
    user3 = User("", -5)
    arr = (user1, user2, user3)

    for obj in arr:
        print_log.info(f"{obj.name}, {obj.age}")

    user1.name = "Антон"
    user1.age = -20

    user2.name = ""
    user2.age = 40.3

    user3.name = "Вова"
    user3.age = 123

    for obj in arr:
        print_log.info(f"{obj.name}, {obj.age}")


if __name__ == "__main__":
    check_test()
    


