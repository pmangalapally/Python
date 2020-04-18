# Valid phone number is 3 digits - 3 digits - 4 digits
# Example is 123-456-7890

def isPhoneNumber(input_text):

    if len(input_text.strip()) != 12:
        return False

    for pos in range(0,3):
        if not input_text[pos].isdecimal():
            return False
    
    if input_text[3] != '-':
        return False
    
    for pos in range(4,7):
        if not input_text[pos].isdecimal():
            return False
    if input_text[7] != '-':
        return False
    
    for pos in range(8, 11):
        if not input_text[pos].isdecimal():
            return False
    
    return True


print('Is 415-555-4242 a phone number?')
print(isPhoneNumber('415-555-4242'))

print('Is 415-555-42422 a phone number?')
print(isPhoneNumber('415-555-42422'))

print('Is 415-555-424  a phone number?')
print(isPhoneNumber('415-555-424 '))

print('Is Moshi moshi a phone number?')
print(isPhoneNumber('Moshi moshi'))

message = 'I am here for you call me at 222-111-3456 or 234-567-1234 phone numbers.'

for i in range(len(message)):
    chunk = message[i : i+12]

    #print(chunk)
    if isPhoneNumber(chunk):
        print(f'{chunk} is a phone number.')