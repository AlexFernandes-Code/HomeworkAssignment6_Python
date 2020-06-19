def validate(message):
    while True:
        try:
            userInput = int(input(message))       
        except ValueError:
            print("Please type in a integer number.")
            continue
        else:
            return userInput 
            break 

def is_triangle(a, b, c):
    if (a > b + c) or (b > a + c) or (c > a + b):
        print("No")
    else:
        print("Yes")
    
print("Please enter three stick lengths...")
a = validate("Stick 1 length: ")
b = validate("Stick 2 length: ")
c = validate("Stick 3 length: ")  
is_triangle(a, b, c)