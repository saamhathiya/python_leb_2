# Create a file and write to it
with open('example.txt', 'w') as file:
    file.write('Hello, World!')

# Read from the file
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

output:-
