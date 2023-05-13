from prompt_toolkit import prompt


# приветствуем пользователя по имени
def welcome_user() -> str:
    while True:
        name = prompt('May I have your name? ')
# проверка на ввод пустого имени
        if name.strip():
            return f'Hello, {name}!'
        else:
            print("Oops=(\nName can't be empty!")
