from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here's the file {filename}:")
print(txt.read())

print("The filename again:")
file_again = input(">")

txt_again = open(file_again)
print(txt_again.read())
