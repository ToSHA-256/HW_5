from datetime import datetime


# Task 4
def decorat(func):
    def wrapper(*args, **kwargs):
        print("Следующее задание: ")
        start = datetime.now()
        res = func(*args, **kwargs)
        finish = datetime.now()
        print(f"Выполнено за {finish - start}")
        return res

    return wrapper


# Task 1
print((lambda: "не" * bool(int(input("Введи число: ")) % 2) + "чётное")())
print("_" * 50)

# Task 2
list_int = list(map(lambda x: float(x), input("Введите список рациональных чисел через пробел: ").split()))
list_str = list(map(lambda x: str(x), list_int))
print("Список строк: ", list_str)
print("_" * 50)

# Task 3
str_tuple = ("шалаш", "топот", "полиндром")
result_tuple = tuple(filter(lambda x: x[::1] == x[::-1], str_tuple))
print("Из кортежа: ", str_tuple)
print("Выбрали полиндромы", result_tuple)
print("_" * 50)


# Task 4
@decorat
def func_pow(n, y):
    return n ** y


print(f"2**5={func_pow(2, 5)}")
print("_" * 50)


# Task 5*
@decorat
def str_to_num(input_str):
    coef = 1
    remainder = 0
    var_split = input_str.split(".")
    if len(var_split) > 2:
        return "не корректно"
    if var_split[0][0] == "-":
        coef = -1
    whole = int("".join(map(lambda x: x * bool(x.isdigit()), var_split[0])))
    if len(var_split) == 2:
        remainder = int("".join(map(lambda x: x * bool(x.isdigit()), var_split[1])))
        remainder /= 10 ** len(str(remainder))

    return coef * (whole + remainder)


in_str = input("Введите строку для перевода в число\n(например:\n -765.76\n -hg765.jg76): ")
print("Теперь это число: ", str_to_num(in_str))
print("_" * 50)
