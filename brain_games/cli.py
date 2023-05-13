from prompt_toolkit import prompt


def welcome_user() -> str:
    while True:
        #приветствуем пользователя по имени
        name = prompt('May I have your name?')
        #проверка на ввод пустого имени
        if name.strip():
            return f'Hello, {name}!'
        else:
            print("Oops=(\nName can't be empty!")