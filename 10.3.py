def is_even(digit):
    """ Перевірка чи є парним число """
    if digit %2 == 0:
        return True
    else:
        return False
assert is_even(2) == True
assert is_even(5) == False
assert is_even(0) == True
print('OK')