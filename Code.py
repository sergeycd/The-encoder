# Напишите декоратор obfuscator
def main():

    def obfuscator(func):
        def wrapper():
            call_func = func()
            make_list_name = list(call_func.get('name','Ключ отсутствует'))
            make_list_password = len(list(call_func.get('password','Ключ отсутствует')))* '*'
            for i in range(1, len(make_list_name)-1):
                make_list_name[i] = '*'
            call_func.update({"name": "".join(make_list_name), "password": make_list_password}) 
            return call_func
        return wrapper

    @obfuscator
    def get_credentials():
        return {
            'name': 'StasBasov',
            'password': 'iamthebest'
        }


    print(get_credentials())


if __name__ == "__main__":
    main()