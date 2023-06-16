import math

def compute_result(x):
    if x < 0.2:
        y = math.sin(x)**2 + math.cos(x**2)
    else:
        y = math.cos(x) + math.exp(math.sqrt(x**2 + 0.1))
    return y

try:
    x = float(input("Введите числовое значение x: "))
    result = compute_result(x)
    print("Результат: ", result)
except ValueError:
    print("Ошибка: Некорректный ввод числового значения x.")
except Exception as e:
    print("Ошибка:", str(e))
