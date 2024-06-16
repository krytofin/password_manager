import json
import hashlib

from datetime import date


class User:
    __NUM_TO_CHECK = 7
    
    def __init__(self) -> None:
        self.__hash_alg = hashlib.sha256()
    
    @staticmethod
    def genetate_sec_key(key:str) -> str:
        return 
    
    def register(self, login: str, password:str):
        self.__hash_alg.update(str(password).encode())
        password = self.__hash_alg.hexdigest()
        secret_key = self.genetate_sec_key(login+password)

    
    def login(self):
        with open('cache.json', 'r') as file:
            last_date = json.load(file)['last_login']
        self.__current_date = sum(map(int, str(date.today()).split('-')))
        if self.__current_date - last_date <= self.__NUM_TO_CHECK:
            ...
            # Успешный вход
            self.__is_login = True
        else:
            # Ввод логина и пароля
            self.__is_login = True
        
    
    
    
if __name__ == '__main__':
    user = User()
    user.register('admin', '1235')
