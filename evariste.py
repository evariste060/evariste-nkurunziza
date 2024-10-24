
def camel_to_snake(camel_case):
    snake_case=''# initialize empty string
    for char in camel_case:
    
        if char.isupper():
            snake_case += ("_")
            snake_case += (char.lower())
        else:
             
            snake_case += (char)
        return snake_case.lstrip('_')
camel_case_input=input("enter variable name in camel case: ")#prompt user for input in camel case

print("snake case:",camel_to_snake(camel_case_input))#output to snake case
