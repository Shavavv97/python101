def print_hi(name):
    print(f'Hi, {name}')

def sets():
    se = { "a", "b", "c",}
    for s in se:
        print(s)

def dictionaries():
    example_dict = { "str": "this is a string", "float": 1.54, "int": 1 }
    for key, val in example_dict.items():
        print(f"{key} = {val}")

def iterate():
    for x in range(10):
        print(x)
    
    fruits = ["apple", "banana", "cherry"]
    for x in fruits:
        if x == "banana":
            break
        print(x)

    for y in range(0, 6, 2):
        print(y)

def printNum():
    x = 1
    f = 1.1

def printStr():
    x = 'Hola'
    y = "Salvador"

if __name__ == "__main__":
    print_hi('Salvador')
