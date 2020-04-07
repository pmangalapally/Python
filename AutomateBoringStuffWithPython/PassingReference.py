# Reference work differently for mutable lists and immuatble variables.
spam = 42
cheese = spam

print(f"spam = {spam}")
print(f"cheese = {cheese}")

spam = 100

print(f"spam = {spam}")
print(f"cheese = {cheese}")

#lists
spam_list = [0, 1, 2, 3, 4]
cheese_list = spam_list
spamcopy_list = spam_list[:]

print(f"spam = {spam_list}")
print(f"cheese = {cheese_list}")
print(f"spamcopy = {spamcopy_list}")

cheese_list.append('Hello!')
print(f"spam = {spam_list}")
print(f"cheese = {cheese_list}")
print(f"spamcopy = {spamcopy_list}")

def eggs(SomeParameters):
        SomeParameters.append('Hello')

spam_fn = [1,2,3]
print(f"spam = {spam_fn}")
eggs(spam_fn)
print(f"spam = {spam_fn}")

#copy and deepcopy
import copy

list_original = [0, 1, 2, 3, 4]
print(f"list_original: {list_original}")

#copy.copy() is used copy lists that does not have inner lists.
list_copy = copy.copy(list_original)
print(f"Before making the changes list_copy: {list_copy}")

list_copy.remove(4)

print(f"After making the change list_copy: {list_copy}")

nested_list_original = [1, [2, 3, 4], 5, 6]
print(f"nested_list_original: {nested_list_original}")

#copy.deepcopy() is used copy lists that have inner lists.
nested_list_original_copy = copy.copy(nested_list_original)
print(f"Before making the changes list_copy: {nested_list_original_copy}")

nested_list_original_copy.remove(6)

print(f"After making the change list_copy: {nested_list_original_copy}")