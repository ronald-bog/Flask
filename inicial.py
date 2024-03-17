## sudo apt install python3-venv
## sudo apt install python3-pip


# Definición del decorador
def my_decorator(func):
    def wrapper():
        print("Antes de llamar a la función")
        func()
        print("Después de llamar a la función")

    return wrapper


# Uso del decorador
@my_decorator
def say_hello():
    print("Hola, mundo!")


# Llamada a la función decorada
say_hello()
