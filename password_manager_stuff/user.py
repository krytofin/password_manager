import json
import hashlib

from datetime import date


class User:
    __NUM_TO_CHECK = 7

    def __init__(self) -> None:
        self.__hash_alg = hashlib.sha256()

    @staticmethod
    def genetate_sec_key(key: str) -> str:
        return

    def register(self, login: str, password: str):
        self.__hash_alg.update(str(password).encode())
        password = self.__hash_alg.hexdigest()
        secret_key = self.genetate_sec_key(login + password)

    def login(self):
        with open("cache.json", "r") as file:
            last_date = json.load(file)["last_login"]
        self.__current_date = sum(map(int, str(date.today()).split("-")))
        if self.__current_date - last_date <= self.__NUM_TO_CHECK:
            ...
            # Успешный вход
            self.__is_login = True
        else:
            # Ввод логина и пароля
            self.__is_login = True

    @staticmethod
    def vigenere(text: str, key: str, encrypt=True):

        result = ""

        for i in range(len(text)):
            letter_n = ord(text[i])
            key_n = ord(key[i % len(key)])

            if encrypt:
                value = (letter_n + key_n) % 1114112
            else:
                value = (letter_n - key_n) % 1114112

            result += chr(value)

        return result

    def vigenere_encrypt(self, text: str, key: str):
        return self.vigenere(text=text, key=key, encrypt=True)

    def vigenere_decrypt(self, text: str, key: str):
        return self.vigenere(text=text, key=key, encrypt=False)


if __name__ == "__main__":
    user = User()
    user.register("admin", "1235")
