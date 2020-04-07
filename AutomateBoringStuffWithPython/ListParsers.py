def list_parser (list_input):
    string_output = ''
    list_length = len(list_input)
    if list_length >= 1:
        list_index = 0
        for list_index in range(list_length):
            if list_length == 1 or list_index == 0:
                string_output = str(list_input[list_index])
            elif list_index < list_length - 1 and list_length >= 2:
                string_output = string_output + ', ' + str(list_input[list_index])
            else:
                string_output = string_output + ', and ' + str(list_input[list_index])
    else:
        string_output = f"List {list_input} is empty"
    
    return string_output

spam = [1, 2, 3, 4, 5, 6]
print(spam)
print(list_parser(spam))

spam = [1]
print(spam)
print(list_parser(spam))

spam = [1, 2]
print(spam)
print(list_parser(spam))

spam = []
print(spam)
print(list_parser(spam))