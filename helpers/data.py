import random
class Data:
    @staticmethod
    def create_new_email_for_registration():
        return f'YuriAkimov17{random.randint(100,999)}@yandex.ru'
    @staticmethod
    def create_new_password_for_registration():
        return f'Qwerty{random.randint(100,999)}'