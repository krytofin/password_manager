import secrets



class PasswordManager:
    def __init__(self, ps, login, password) -> None:
        self.__secret_code = secrets.token_hex(64)
        
    def get_secret(self):
        return self.__secret_code
        
        
        
pm = PasswordManager('123', '123', '123')
print(pm.get_secret())