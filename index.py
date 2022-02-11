
def addition(a,b):
    return a + b

def soustraction(a,b):
    if b > a:
        return "on ne peut pas avoir un nombre négatif"
    else:
        return a - b




print(addition(5,5))

print('------------------------------------------')
print('Soustraction')
print(soustraction(10,2))