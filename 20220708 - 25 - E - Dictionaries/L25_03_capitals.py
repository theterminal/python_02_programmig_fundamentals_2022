# 20220713 - Python Code - Dictionaries - Exercise
# 03 - Capitals - judge url: https://judge.softuni.org/Contests/Compete/Index/1737#2


# ------------- version 2 --------- comprehension, no zip ----------- judge: 100%

countries = input().split(', ')
cities = input().split(', ')

result = {countries[i]: cities[i] for i in range(len(cities))}

for k, v in result.items():
    print(f'{k} -> {v}')


# ------------- version 1 --------- no comprehension, with zip ---------- judge: 100%

countries = input().split(', ')
cities = input().split(', ')

for country, city in zip(countries, cities):
    print(country, '->', city)


# ------------- version 3 --------- no comprehension, with zip ---------- judge: 100%

countries = input().split(', ')
cities = input().split(', ')

result = dict(zip(countries, cities))
for country, city in result.items():
    print(country, '->', city)
