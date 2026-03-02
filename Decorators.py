from Main import Person


def myDecorator(function):

    def wrapper(*args, **kwargs):
        print("I m decorating your function")
        function(*args, **kwargs)

    return wrapper

@myDecorator
def helloWorld(Person):
    print(f"Hello {Person}")

helloWorld("Utsav")