from typing import Dict, List


# person = {
#     "name": "Vytautas",
#     "surname": "Sluckas",
#     "ip": "127.0.0.1",
#     "programming_language": "python",
#     "address": {"Street": "some street", "House Number": "some house number"},
#     "languages": ["Lithuanian", "English", "Norwegian"],
# }

# person1 = {
#     "name": "Tomas",
#     "surname": "BLABLABA",
#     "ip": "127.0.0.1",
#     "programming_language": "python",
#     "address": {"Street": "some street", "House Number": "some house number"},
#     "languages": ["Latvian", "English", "Swedish"],
# }

# people = [person, person1]

# # print(people)


# def get_most_popular_language(people: List[Dict]) -> str:
#     language_counts = {}
#     languages_list = []
#     for person in people:
#         languages_list.append(person["languages"])

#     languages_list = languages_list[0] + languages_list[1]
#     unique_languages_set = sorted(set(languages_list))

#     for item in unique_languages_set:
#         language_counts[item] = languages_list.count(item)

#     return max(language_counts)

# dict_one = {"a": 10, "b": 20, "c": 30}
# dict_two = {"a": 5, "b": 6, "d": 400}


# def custom_dictionary_update(
#     first_dictionary: Dict, second_dictionary: Dict, overwrite: bool = False
# ) -> Dict:
#     if overwrite == True:
#         first_dictionary.update(second_dictionary)
#     else:
#         for key, value in second_dictionary.items():
#             if key in first_dictionary:
#                 first_dictionary[key] += value
#         else:
#             first_dictionary[key] = value
#     return first_dictionary


# print(dict_one, dict_two.items())
# print(custom_dictionary_update(dict_one, dict_two))


# person = {
#     "name": "Vytautas",
#     "surname": "Sluckas",
#     "ip": "127.0.0.1",
#     "programming_language": "python",
#     "address": {"Street": "some street", "House Number": "some house number"},
#     "languages": ["Lithuanian", "English", "Norwegian"],
# }

# person1 = {
#     "name": "Tomas",
#     "surname": "BLABLABA",
#     "ip": "162.2.0.2",
#     "programming_language": "python",
#     "address": {"Street": "some street", "House Number": "some house number"},
#     "languages": ["Latvian", "English", "Swedish"],
# }

# person2 = {
#     "name": "Tom",
#     "surname": "Edison",
#     "ip": "127.2.0.1",
#     "programming_language": "python",
#     "address": {"Street": "some street", "House Number": "some house number"},
#     "languages": ["Latvian", "English", "Swedish"],
# }


# people = [person, person1, person2]


# def find_ip(people: List[dict]) -> list:
#     return [person for person in people if person["ip"].split(".")[1] == "2"]


# print(find_ip(people))

# a: int = 2
# b: int = 3


# def calculate_area(length: int, width: int) -> int:
#     return length * width


# # print(calculate_area(a, b))


# def power_value(base: int, exponent: int = 2) -> int:
#     return base**exponent


# # print(power_value(a, b))


# def calculate_sum(*args) -> int:
#     return sum(args)


# # print(calculate_sum(2, 2, 3))


# def factorial(n: int) -> int:
#     if n == 1:
#         return n
#     else:
#         return n * factorial(n - 1)


# print(factorial(4))

# # 1
# result = [x**2 for x in range(1, 11)]

# print(result)

# # 2
# result = [x for x in range(1, 11) if x % 2 == 0]

# print(result)

# # 3
# result = {x: x**3 for x in range(1, 6)}

# print(result)

# 4
# result = [x**2 for x in range(1, 21) if x % 3 != 0 and x % 4 != 0]

# print(result)

# 5
# original_list = [5, 15, 8, 20, 12, 7, 18]
# result = [(ind, x) for ind, x in enumerate(original_list) if x >= 10]

# print(result)

# 6
# names = ["Alice", "Bob", "Charlie", "David"]
# ages = [25, 30, 35, 40]

# result = {names[x]: ages[x] for x in range(len(names)) if len(names[x]) > 4}
# print(result)
