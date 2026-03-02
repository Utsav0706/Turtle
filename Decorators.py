def myDecorator(function):

    def wrapper():
        print("I m decorating your function")
        function()

    return wrapper

def helloWorld():
    print("Hello World")

myDecorator(helloWorld)