import pprint
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0)
    #print(character, count[character])
    count[character] = count[character] + 1

pprint.pprint(count)

count.setdefault('child_dictionary', {1,2,3,4})
print(pprint.pformat(count))