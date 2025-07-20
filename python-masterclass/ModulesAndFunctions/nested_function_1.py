def greet_python(items: list) -> None:
    greeting = 'Hello'

    def make_greeting(item: str) -> str:
        return f'{greeting} {item}'

    for item in items:
        print(make_greeting(item))


names = ['John', 'Eric', 'Graham', 'Terry', 'Terry', 'Michael']

greet_python(names)
