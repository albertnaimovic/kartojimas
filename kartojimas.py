from typing import List


def calculate_total_salary(base_salary: int, *args, **kwargs) -> int:
    return base_salary + sum(args) + sum(kwargs.values())


# Test cases
# print(calculate_total_salary(50000))  # Test with only base salary
# print(calculate_total_salary(50000, 2000, 3000))  # Test with base salary and additional bonuses
# print(calculate_total_salary(50000, 2000, 3000, health_insurance=1000, travel_allowance=1500))  # Test with kwargs


def create_greeting(name: str, greeting: str = "Hello", **kwargs):
    if kwargs:
        formatted_kwargs: str = ""
        for key in kwargs:
            formatted_kwargs += key + " = " + str(kwargs[key]) + ", "
        formatted_kwargs = formatted_kwargs[:-2] + "."
        return f"{greeting}, {name}, {formatted_kwargs}"

    else:
        return f"{greeting}, {name}."


# Test cases
# print(create_greeting("Alice"))  # Test with mandatory argument only
# print(create_greeting("Bob", "Hi"))  # Test with default parameter and mandatory argument
# print(create_greeting("Charlie", age=30, location="New York"))  # Test with additional keyword arguments


def generate_shopping_list(*args, title: str = "My shopping list:") -> str:
    formatted_args: str = ""
    for x in args:
        formatted_args += x + ", "
    formatted_args = formatted_args[:-2] + "."
    return f"{title} {formatted_args}"


# print(generate_shopping_list("asdad", "asdada", "qrq", title="pavadinimas"))
# print(generate_shopping_list("asdad", "asdada", "qrq"))


def get_average(my_list: List[int]) -> float:
    if type(my_list) != list:
        raise TypeError("Input is not list")
    for num in my_list:
        if type(num) != int:
            raise TypeError("Elements in list should be integers")
    return sum(my_list) / len(my_list)


# try:
#     print(get_average([1, 2, "3", 4, 5]))
# except Exception as err:
#     print(f"You got an error: {err}")


# Write a function that takes a list of integers and returns their average.
# Raise a TypeError if the input is not a list or if any element in the list is not an integer.
# Provide a solution that addresses this error.

# numbers = [5, 47, 6, 485, 1, 521, 8, 184, 1, 7, 5, 52, 562]
# numbers_not = [5, 47, 6, 485, 1, "a", 8, 184, 1, 7, 5, 52, 562]
# numbers_not_again = "5, 47, 6, 485, 1, 521, 8, 184, 1, 7, 5, 52, 562"
# def calculate_average(numb: list) -> float:
#     if type(numb) is not list or not numb:
#         raise TypeError("Not a list or is empty list")
#     numb_check = [x for x in numb if type(x) == int]
#     # print(numb_check)
#     if numb_check != numb:
#         raise TypeError("Not all items of the list are integers")
#     return round((sum(numb) / len(numb)), 2)
# def try_calculate_averages(*args: list) -> list:
#     averages = []
#     for arg in args:
#         try:
#             averages.append(calculate_average(arg))
#         except TypeError as e:
#             if str(e) == "Not a list or is empty list":
#                 print("Not a list or is empty list")
#             elif str(e) == "Not all items of the list are integers":
#                 print("Not all items of the list are integers")
#                 try:
#                     fixed_list = [int(x) for x in arg]
#                     averages.append(calculate_average(fixed_list))
#                 except ValueError:
#                     print("Unable to quickfix your problem!")
#         except Exception as e:
#             print(f"Unexpected problem {e}")
#     return averages
# print(try_calculate_averages(numbers, numbers_not, numbers_not_again))


def read_file(file):
    return file.read()

try:
    file = open("demo.txt", "r")
    print(read_file(file))
except FileNotFoundError:
    print("File not found")
