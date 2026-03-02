from Main import Person


def myDecorator(function):

    def wrapper(*args, **kwargs):
        print("I m decorating your function")
        return function(*args, **kwargs)

    return wrapper

@myDecorator
def helloWorld(Person):
    print(f"Hello {Person}")

print(helloWorld("Utsav"))