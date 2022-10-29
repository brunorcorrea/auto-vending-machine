from paprika import *


@data
class Person:
    name: str
    age: int


if __name__ == '__main__':
    person = Person("bruno", 18)
    print(person)
