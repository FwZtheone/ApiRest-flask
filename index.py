
def addition(a,b):
    return a + b

def soustraction(a,b):
    if b > a:
        return "on ne peut pas avoir un nombre négatif"
    else:
        return a - b


def division(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "You can't divide by zero!"


def multiplication(a,b):
    return a  *  b

def hello():
    print("hello world")

print(addition(5,5))

print('------------------------------------------')
print('Soustraction')
print(soustraction(10,2))
print('------------------------------------------')
print('Division')
print(division(100,2))
print('------------------------------------------')
print('Multiplication')
print(division(10,2))


hello()