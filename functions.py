from math import pi
from functools import reduce
from operator import add


def add_number(x: int, y: int) -> int:
    return x + y


print(add_number(10, 20))

# types
radius = 5.5

print("Distance circle is: {0}".format(2 * pi * radius))

# string
name = "jemesson"
lastname = "lima"

# string format
print("My name is {0} {1}".format(name.capitalize(), lastname.capitalize()))

# interpolation
print(f"My name is {name.capitalize()} {lastname.capitalize()}")

# conditions
age = 27
adult = 18

if not name.isalpha():
    print(name.isdigit())

print("Go to the cinema") if(age >= adult) else print("Go to home")

# lists
x = 10
for index in range(1, 10, 2):
    x += 10
    print("x = {0}".format(x))

students = ["Ana", "Gileno", "Jemesson", "Herbert", "Eric"]
for student in students:
    if "Jemesson" in student:
        continue
    print(student)

del(students[-1])

student_excelents = students[1:-1]
print("{0}\n{1}".format(len(student_excelents), student_excelents))

# dictionary
student = {
    "id": 1,
    "name": "Jemesson",
    "age": 27,
    "married": None
}

student1 = {
    "id": 2,
    "name": "Jimens",
    "age": 35,
    "married": True
}

students_cesar = [
    student,
    student1
];

for student in students_cesar:
    print(student.values())

# tuple and set
print([(x, x**2) for x in range(6)])
print([str(round(pi, i)) for i in range(1, 6)])

print(set([3, 2, 1, 3, 5]))

# exception

try:
    student["last_name"] = "Lima"
    last_name = student["last_name"]
    # numbered_lastname = 3 + last_name
except KeyError:
    print("error finding last_name")
except TypeError as e:
    print("i cant add these two together")
    print(e)
except Exception:
    print("generic error")

y = [round(pi * pow(r, 2), 5) for r in range(1, 10)]
print(y)

# lambda example
f = lambda x, y: x + y
print(f(2, 3))

# map example - map(func, seq)
c = [39.5, 35, 27, 30]
f = list(map(lambda x: round((float(9)/5) * x + 32, 3), c))
print(c)
print(f)

# filter - filter(function, list)
fib = [0, 1 , 1, 2, 3, 5, 8, 13, 21, 34, 55]
result = list(map(lambda x: pow(x, 2), list(filter(lambda val: val % 2 == 0, fib))))

# get the max of a list
f = lambda a,b: a if a > b else b
res = reduce(f, [-1, 29.99, 29.999, 3.3])

# operator add
y = reduce(add, map(int, filter(lambda num: num.isnumeric(), "3+4+5+6++".split("+"))))
print(y)
