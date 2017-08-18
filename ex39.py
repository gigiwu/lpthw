states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print('-' *10)
for state, code in list(states.items()):
    print(f"{state} abbr: {code}  city: {cities[code]}")


# print a defautl value
city = cities.get("TX", "Does not exist")
print(f"The city of Texas is: {city}")

city = cities.get("NY", "Does not exist")
print(f"The city of New York is: {city}")
