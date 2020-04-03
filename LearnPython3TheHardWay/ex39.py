# create a mapping of state to abbrevation
states = {
    'Oregon' : 'OR',
    'Florida' : 'FL',
    'California' : 'CA',
    'New York' : 'NY',
    'Michigan' : 'MI'
}

# create a basic set of states and some cities in them
cities = {
    'CA' : 'San Franscisco',
    'MI' : 'Detroit',
    'FL' : 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#print out some cities
print('-' * 10)
print("NY state has: ", cities['NY'])
print("OR state has: ", cities['OR'])

#print out some states
print('-' * 10)
print("Michigan's abbrevation is: ", states['Michigan'])
print("Florida's abrevation is: ", states['Florida'])

#do it y using the state then cities dict
print('-' * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

#print every state's abbrevation
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

#print every city in the state
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

#now both at the same time
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('-' * 10)
#safely get a abbreviation by state that might not be there
state = states.get('Texas')

if not state:
    print("Sorry, No Texas")

#get a city with default value
city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is: {city}")
