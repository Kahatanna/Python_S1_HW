# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = bool(input('Введите логическое значение x = '))
y = bool(input('Введите логическое значение y = '))
z = bool(input('Введите логическое значение z = '))

ex1 = not(x and y and z)
ex2 = not(x) or not(y) or not(z)
if ex1 == ex2:
    print('Утверждение верно!')
    print('¬(X ⋁ Y ⋁ Z) = ', ex1) 
    print('¬X ⋀ ¬Y ⋀ ¬Z = ', ex2) 
else:
    print('Что-то пошло не так...')