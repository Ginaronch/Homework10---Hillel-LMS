def pow(x):
    return x ** 2
def some_gen(begin, end, func):
    """
     begin: перший елемент послідовності
     end: кількість елементів у послідовності
     func: функція, яка формує значення для послідовності
    """
    current = begin
    for num in range(end): #4 повтора
        yield current
        current = func(current)
from inspect import isgenerator

gen = some_gen(2, 4, pow) #начиная с 2 сделать четыре цикла по возвведению в квадрат, сохраняя предидущее значение(2, 2*2 = 4, 4*4 = 16, 16*16 = 256)
assert isgenerator(gen) == True
assert list(gen) == [2, 4, 16, 256]
print('OK')