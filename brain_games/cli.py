import prompt


# приветствуем пользователя по имени
def welcome_user():
    name = prompt.string('May i have your name? ')
    return(f"Hello, {name}!")
