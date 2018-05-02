from math import e
from math import pi
from functools import reduce
from operator import add


def print_word_times(word: str, times: int) -> str:
    return word * times


def add_number(x: int, y: int) -> int:
    return x + y


def delta_function(a, b, c):
    delta = (b**2 - 4 * a * c) / (2 * a)
    return delta


def is_possible_cinema(age, adult=18):
    return "Go to the cinema" if (age >= adult) else "Go to home"


def square_list_range(numbers):
    result = []
    for i in range(0, len(numbers)):
        result.append(numbers[i] * numbers[i])
    return result


def square_list(numbers):
    return [i ** 2 for i in numbers]


def get_word_lower(word: str) -> str:
    word_list = list(word)

    for i in range(0, len(word_list)):
        word_list[i] = word_list[i].lower()

    return "".join(word_list)


def count_char_appear(word: str) -> dict:
    dict_char = {}
    list_chars = list(word)

    for char in list_chars:
        if char in dict_char:
            dict_char[char] += 1
        else:
            dict_char[char] = 1

    return dict_char

print(print_word_times("Jem ", 5))
print(add_number(10, 20))
print(f"Delta result = {delta_function(2, 4, 1)}")

# types
radius = 5.5

print("Distance circle is: {0}".format(2 * pi * radius))

# strings
name = "jemesson"
lastname = "lima"
city = "recife"
area = 2.5

print("My name is {0} {1}".format(name.capitalize(), lastname.capitalize()))

print(f"My name is {name.capitalize()} {lastname.capitalize()}")
print(f"I live in {city.capitalize()} which area is {area} km2")

string = "Hello world... I am coding now"
lookup = "I"

print(string[string.find(lookup):])

string = "arara"
print("palindrome" if string == string[::-1] else "non palindrome")

# conditions
age = 20

if not name.isalpha():
    print(name.isdigit())

print(is_possible_cinema(age, adult=21))
print(square_list_range([1, 2, 3, 4]))
print(square_list([1, 2, 3, 4]))
print(get_word_lower("HeLLo WORld"))

# lists
x = 10
for index in range(1, 10, 2):
    x += 10 + index
    print("x = {0}".format(x))

students = ["Ana", "Gileno", "Jemesson", "Herbert", "Eric"]
for student in students:
    if "Jemesson" in student:
        continue
    print(student)

students = sorted(students)
students.remove(students[-1])
print(students)

student_excelents = students[1:-1]
print("great students: {0}\n{1}".format(len(student_excelents), student_excelents))

# dictionary
print(count_char_appear("Hello World =)"))

student = {
    "id": 1,
    "name": "Jemesson",
    "age": 27,
    "married": False
}

student1 = {
    "id": 2,
    "name": "Jimens",
    "age": 35,
    "married": True
}

cesar_studentes = [
    student,
    student1
]

for student in cesar_studentes:
    print(student.keys())
    print(student.values())
    print(student.items())

# tuple and set
print([(x, x**2, x**3) for x in range(0, 6, 2)])
print([str(round(pi, i)) for i in range(1, 6)])

print(set([3, 2, 1, 3, 5]))

# exception

try:
    if "last_name" not in student:
        student["last_name"] = "Lima"
    print(3 * student["last_name"])
except KeyError:
    print("error finding last_name")
except TypeError as e:
    print("i cant add these two together")
    print(e)
except Exception:
    print("generic error")

fx = [(round(pow(e, i), 3), round(pow(pi, i), 3)) for i in range(1, 10)]
print(fx)

# lambda example
f = lambda x, y: x + y
print(f(2, 3))

# Map, Filter and Reduce.
c = [39.5, 35, 27, 30]
f = list(map(lambda x: round((float(9)/5) * x + 32, 3), c))
print(f"celsius temperatures: {c}")
print(f"fahrenheit temperatures: {f}")

fib = [0, 1 , 1, 2, 3, 5, 8, 13, 21, 34, 55]
result = list(map(lambda x: pow(x, 2), list(filter(lambda val: val % 2 == 0, fib))))
print(result)

# get the max of a list
f = lambda a,b: a if a > b else b
res = reduce(f, [-1, 29.99, 29.999, 3.3])
print(res)

# operator add
y = reduce(add, map(int, filter(lambda num: num.isnumeric(), "3+4+5+6++".split("+"))))
print(y)
